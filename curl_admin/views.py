from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from curl_admin.forms import *
from django.urls import reverse_lazy
from users.decorators import adminonly, allowed_users
from curl_admin.models import Appointment, Customer, Services
from django.db.models import Sum

import stripe
stripe.api_key = "sk_test_51KXemoSJ2J4TjDBaYXn0GhYiu7LT8JS4erXkKJINAc16tZRtRFO7TJxzHqvOJFaJUtNvQ5ADHK7sbhgTUxzyzwNI00yQu7KKV9"


def charge(req):
    amount = 5
     
    if req.method == 'POST':
        pass
        
    


@login_required(login_url='business-login')
@adminonly
def dashboard(req):
    apps = Appointment.objects.filter(user_id = req.user.id)
    context = {'apps':apps}
    return render(req,'curl_admin/dashboard.html',context)


class AddCustomer(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'curl_admin/customers.html'
    success_url = reverse_lazy('customers')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['customers'] = Customer.objects.all()
        data.setdefault('action','add')
        return data
    
    def form_valid(self, form: CustomerForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class CustomerListView(ListView):
    model=Customer
    template_name='curl_admin/customers.html'
    context_object_name='customers'

    

class CustomerUpdateView(UpdateView):
    model = Customer
    #template_name = "foodapp/foodform.html"
    template_name='curl_admin/customers.html'
    form_class=CustomerForm
    success_url=reverse_lazy('customers')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['customers']=Customer.objects.all()
        return  data

class CustomerDeleteView(DeleteView):
    model=Customer
    success_url=reverse_lazy('customers')

# Appointments Section 

class AppointmentListView(ListView):
    model=Appointment
    template_name='curl_admin/appointments.html'
    context_object_name='appointments'
    
def bookapp(req,cust_id):
    customer = Customer.objects.get(pk=cust_id)
    if req.method == 'POST':
        form = AppointmentForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('appointments')
    form = AppointmentForm(initial={'customer':customer})
    context = {'form':form,'action':'add'}
    return render(req,'curl_admin/appointments.html',context)
    
    
# CBV Book-Appointment    
    
# class BookAppointmentView(CreateView):
#     model = Appointment
#     form_class = AppointmentForm
#     template_name = 'curl_admin/appointments.html'
#     success_url = reverse_lazy('appointments')
    
#     def get_context_data(self,**kwargs):
#         data = super().get_context_data()
#         data['appointments'] = Appointment.objects.all()
#         data.setdefault('action','add')
#         return data
    
#     def form_valid(self, form: AppointmentForm):
#         form.instance.customer = self.customer.cust_name
#         return super().form_valid(form)
    
class AppointmentUpdateView(UpdateView):
    model = Appointment
    #template_name = "foodapp/foodform.html"
    template_name='curl_admin/appointments.html'
    form_class=AppointmentForm
    success_url=reverse_lazy('appointments')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['appointments']=Appointment.objects.all()
        return  data

class AppointmentDeleteView(DeleteView):
    model=Appointment
    success_url=reverse_lazy('appointments')
    
# Services 

class AddServiceView(CreateView):
    model = Services
    form_class = ServiceForm
    template_name = 'curl_admin/services.html'
    success_url = reverse_lazy('services')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['services'] = Services.objects.all()
        data.setdefault('action','add')
        return data
    
    def form_valid(self, form: ServiceForm):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ServicesListView(ListView):
    model=Services
    template_name='curl_admin/services.html'
    context_object_name='services'

    

class ServiceUpdateView(UpdateView):
    model = Services
    #template_name = "foodapp/foodform.html"
    template_name='curl_admin/services.html'
    form_class=ServiceForm
    success_url=reverse_lazy('services')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['services']=Services.objects.all()
        return  data

class ServiceDeleteView(DeleteView):
    model=Services
    success_url=reverse_lazy('services')
    
# Employee Department 

class AddDepartmentView(CreateView):
    model = EmpDept
    form_class = EmpDeptForm
    template_name = 'curl_admin/employees.html'
    success_url = reverse_lazy('employees')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['employees'] = Employee.objects.all()
        data.setdefault('action','deptadd')
        return data
    
    def form_valid(self, form: EmpDeptForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# Employees 

class AddEmployeeView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'curl_admin/employees.html'
    success_url = reverse_lazy('employees')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['employees'] = Employee.objects.all()
        data['empdept'] = EmpDept.objects.all()
        data.setdefault('action','add')
        return data
    
    def form_valid(self, form: EmployeeForm):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EmployeesListView(ListView):
    model=Employee
    template_name='curl_admin/employees.html'
    context_object_name='employees'

    

class EmployeeUpdateView(UpdateView):
    model = Employee
    #template_name = "foodapp/foodform.html"
    template_name='curl_admin/employees.html'
    form_class=EmployeeForm
    success_url=reverse_lazy('employees')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['employees']=Employee.objects.all()
        return  data

class EmployeeDeleteView(DeleteView):
    model=Employee
    success_url=reverse_lazy('employees')
    
    
# Business View 

class RegisterBusiness(CreateView):
    model = Business
    form_class = BusinessRegisterationForm
    template_name = 'curl_admin/business.html'
    success_url = reverse_lazy('business')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['business'] = Business.objects.all()
        data.setdefault('action','add')
        return data
    
    def form_valid(self, form: BusinessRegisterationForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BusinessListView(ListView):
    model=Business
    template_name='curl_admin/business.html'
    context_object_name='business'

class BusinessUpdateView(UpdateView):
    model = Business
    #template_name = "foodapp/foodform.html"
    template_name='curl_admin/business.html'
    form_class=BusinessRegisterationForm
    success_url=reverse_lazy('business')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['business']=Business.objects.all()
        return  data

class BusinessDeleteView(DeleteView):
    model=Business
    success_url=reverse_lazy('business')
    
    
# Checkout 

def checkout(req,id):
    app = Appointment.objects.get(pk = id)
    if app.customer:
        customer = Customer.objects.get(pk = app.customer.cust_id)
    else:
        customer = MyUser.objects.get(pk = app.ucustomer.id)
    services = app.services.all()

    total_amount = app.services.aggregate(total = Sum('serv_price'))
    
    context = {'customer' : customer,'services': services,'app' : app,'total_amount': total_amount}
    return render(req,'curl_admin/checkout.html',context)


# Business Hours 

class AddBhour(CreateView):
    model = BusinessHours
    form_class = BusinessHourForm
    template_name = 'curl_admin/business.html'
    success_url = reverse_lazy('business')
    
    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['business'] = Business.objects.all()
        data.setdefault('action','add')
        return data
    
    def form_valid(self, form: BusinessHourForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BhourListView(ListView):
    model=BusinessHours
    template_name='curl_admin/business.html'
    context_object_name='bhour'

    

class BhourUpdateView(UpdateView):
    model = BusinessHours
    #template_name = "foodapp/foodform.html"
    template_name='curl_admin/business.html'
    form_class=BusinessHourForm
    success_url=reverse_lazy('business')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        data['business']=Business.objects.all()
        return  data

class BhourDeleteView(DeleteView):
    model=BusinessHours
    success_url=reverse_lazy('business')