
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from curl_admin.forms import AppointmentForm, CustomerForm
from curl_admin.models import Business, Customer
from curls.forms import UserAppointmentForm
from users.models import MyUser
from .models import *
from users.decorators import allowed_users

# Create your views here.

def curls(req):
    businesses = Business.objects.all()
    context = {'businesses':businesses}
    return render(req,'curls/curls.html',context)

def userpage(req):
    context = {}
    return render(req,'curls/userpage.html',context)

@login_required(login_url='user-login')
def bookapp(req,b_id):
    business = Business.objects.get(b_id = b_id)
    user = business.user_id
    # ucustomer = MyUser.objects.get(pk=user_id)
    ucustomer = req.user.id
    
    if req.method == 'POST':
        form = UserAppointmentForm(req.POST,user_id=user,ucustomer=ucustomer)
        if form.is_valid():
            form.save()
            return redirect('curls')
        
    
    form = UserAppointmentForm(user_id=user,ucustomer=ucustomer,initial={'ucustomer':ucustomer})                        #initial={'ucustomer':ucustomer}
    context = {'form':form,'action':'add'}
    return render(req,'curls/businessDetail.html',context)


def business_detail(req,b_id):
    business = Business.objects.get(b_id = b_id)
    context = {'business': business}
    return render(req,'curls/businessDetail.html',context)