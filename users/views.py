from django.shortcuts import redirect, render
from django.views.generic import CreateView, UpdateView, ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.decorators import login_required
from users.forms import *
from users.models import MyUser
from .decorators import unauthenticated_user



# Business Authentication 

@unauthenticated_user
def bregister(req):
    form = BusinessForm()
    
    if req.method == 'POST':
        form = BusinessForm(req.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            
            group = Group.objects.get(name='Business')
            user.groups.add(group)
            
            messages.success(req,'Business Account Created!')
            return redirect('business-login')
            
    context = {'form':form}
    return render(req,'auth/signup.html',context)


@unauthenticated_user
def blogin(req):
    
    if req.method == 'POST':
        context = {}  
        contact =  req.POST.get('contact')
        password = req.POST.get('password')  
        
        user = authenticate(req, username=contact,password = password)
        
        if user is not None:
            login(req, user)
            return redirect('dashboard')
        else:
            messages.info(req, 'Mobile Number or Password is incorrect..')
     
    context = {}  
    return render(req,'auth/login.html',context)
 
def userlogout(req):
    logout(req)
    return redirect('curls')


 
#  Customer Authentication 

@unauthenticated_user
def uregister(req):
    form = CustomerForm()
    
    if req.method == 'POST':
        form = CustomerForm(req.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            
            group = Group.objects.get(name='Customer')
            user.groups.add(group)
            
            messages.success(req,'Account Created!')
            return redirect('user-login')
            
    context = {'form':form}
    return render(req,'curls/signup.html',context)

@unauthenticated_user
def ulogin(req):
    
    if req.method == 'POST':
        context = {}  
        contact =  req.POST.get('contact')
        password = req.POST.get('password')  
        
        user = authenticate(req, username=contact,password = password)
        
        if user is not None:
            login(req, user)
            return redirect('curls')
        else:
            messages.info(req, 'Mobile Number or Password is incorrect..')
     
    context = {}  
    return render(req,'curls/login.html',context)

# User signup using CBV
# class UserSignup(CreateView):
#     model = MyUser
#     form_class = UserForm
#     template_name = 'auth/signup.html'
#     success_url = reverse_lazy('business-login')
    


class BusinessProfileView(ListView):
    model=MyUser
    template_name='curl_admin/profile.html'

class ProfileUpdateView(UpdateView):
    model = MyUser
    template_name='curl_admin/profile.html'
    form_class=ProfileForm
    success_url=reverse_lazy('profile')

    def get_context_data(self,**kwargs):
        data = super().get_context_data()
        data['action']='update'
        return  data