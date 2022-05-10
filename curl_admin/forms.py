from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    
    class Meta:
        
        model = Customer
        fields = ('cust_name','cust_gender','cust_contact','cust_email')
        choices = (
            ('M','Male'),
            ('F','Female')
            )
        widgets = {
            'cust_name' : forms.TextInput(attrs={'placeholder':'Enter Customer Name','class':'form-control'}),
            'cust_gender' :  forms.RadioSelect(choices=choices,attrs={'title':'Gender','class':'list-unstyled'}),
            'cust_contact' : forms.NumberInput(attrs={'placeholder':'Enter Customer Contact','class':'form-control'}),
            'cust_email' : forms.TextInput(attrs={'placeholder':'Enter Customer Email','class':'form-control'}),
        }
        

class AppointmentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        
        self.fields['services'].label = "Services"
        self.fields['app_date'].label = "Appointment Date"
        self.fields['staff'].label = "Staff"
        
    
    class Meta:
        
        model = Appointment
        fields = ('customer','services','app_date','staff')
    
        widgets = {
            'services' :  forms.SelectMultiple(attrs={'class':'list-unstyled'}),
            'app_date' : forms.DateTimeInput(attrs={'type':'datetime-local','placeholder':'Date & Time','class':'form-control'}),
            'staff' :  forms.SelectMultiple(attrs={'class':'list-unstyled'}),
        }
        
        
class ServiceForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['serv_name'].label = "Service Name"
        self.fields['serv_price'].label = "Service Price"
        self.fields['gender'].label = "Service For"
        self.fields['serv_desc'].label = "Service Description"
    
    class Meta:
        
        model = Services
        fields = ('serv_name','serv_price','gender','serv_desc')
        choices = (
            ('M','Male'),
            ('F','Female')
            )
        widgets = {
            'serv_name' : forms.TextInput(attrs={'placeholder':'Enter Service Name','class':'form-control'}),
            'serv_price' : forms.NumberInput(attrs={'placeholder':'Enter Service Cost','class':'form-control'}),
            'gender' :  forms.RadioSelect(choices=choices,attrs={'title':'Gender','class':'list-unstyled'}),
            'serv_desc' : forms.Textarea(attrs={'class':'form-control','placeholder':'Give a cool description to your services to make it stand out..'})
        }

class EmpDeptForm(forms.ModelForm):
    
    class Meta:
        
        model = EmpDept
        fields = ('dept_name',)


        
class EmployeeForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['emp_name'].label = "Employee Name"
        self.fields['emp_gender'].label = "Gender"
        self.fields['emp_contact'].label = "Contact"
        self.fields['role'].label = "Job Role"
        self.fields['emp_dob'].label = "Date of Birth"
        self.fields['emp_doj'].label = "Date of Joining"
        self.fields['emp_salary'].label = "Salary"
        self.fields['dept'].label = "Department"
        self.fields['emp_name'].label = "Employee Name"
    
    class Meta:
        
        model = Employee
        fields = ('profile_pic','emp_name','emp_gender','emp_contact','role','emp_dob','emp_doj','emp_salary','dept')
        choices = (
            ('M','Male'),
            ('F','Female'),
            ('O','Others')
            )
        widgets = {
            'emp_name' : forms.TextInput(attrs={'placeholder':'Enter Employee Name','class':'form-control','label':'Employee Name'}),
            'emp_gender' :  forms.RadioSelect(choices=choices,attrs={'title':'Gender','class':'list-unstyled'}),
            'emp_contact' : forms.NumberInput(attrs={'placeholder':'Enter Employee Contact','class':'form-control'}),
            'role' : forms.TextInput(attrs={'placeholder':'Designation','class':'form-control'}),
            'emp_dob' : forms.DateInput(attrs={'type':'date','placeholder':'Date Of Birth','class':'form-control'}),
            'emp_doj' : forms.DateInput(attrs={'type':'date','placeholder':'Date Of Joining','class':'form-control'}),
            'emp_salary' : forms.NumberInput(attrs={'placeholder':'Salary in Months','class':'form-control'}),
            'dept' : forms.RadioSelect(attrs={'class':'form-control'})
        }
        
class BusinessRegisterationForm(forms.ModelForm):
    
    class Meta:
      model=Business
      fields=('profile_img','b_name','b_contact','b_email','b_address','services','employee','b_hours')
      widgets = {
        'b_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Business Name'}),
        'b_contact': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder': 'Contact'}),
        'b_email': forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'Email'}),
        'b_address': forms.Textarea(attrs={'class': 'form-control form-control-user','placeholder': 'Business Address'}),
        'services' : forms.SelectMultiple(attrs={'class': 'form-control form-control-user','placeholder': 'Services'}),
        'employee' :forms.SelectMultiple(attrs={'class': 'form-control form-control-user','placeholder': 'Employees'}),
        }
      

class BusinessHourForm(forms.ModelForm):
    
    class Meta:
        model=BusinessHours
        fields = '__all__'
        widgets = {
        'open_time': forms.TimeInput(attrs={'type':'time','class': 'form-control form-control-user'}),
        'close_time': forms.TimeInput(attrs={'type':'time','class': 'form-control form-control-user'}),
        }