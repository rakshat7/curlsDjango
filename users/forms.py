from crispy_forms.helper import FormHelper
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser


class BusinessForm(UserCreationForm):
  
  password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Password'}))
  password2 = forms.CharField(label='Confirm password',  widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Confirm Password'}))
    
  def __init__(self, *args, **kwargs):
    super(BusinessForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False 
  
  class Meta:
    
    model = MyUser
    fields = ('first_name','last_name','contact','gender','email','password1','password2')
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'First Name'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Last Name'}),
      'contact': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder': 'Contact Number'}),
      'email': forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'Email'}),
      'gender' : forms.RadioSelect(attrs={'class': 'form-control form-control-user'}), 
    }
    
    
class CustomerForm(UserCreationForm):
  
  password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Password'}))
  password2 = forms.CharField(label='Confirm password',  widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user','placeholder': 'Confirm Password'}))
    
  def __init__(self, *args, **kwargs):
    super(CustomerForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False 
  
  class Meta:
    
    model = MyUser
    fields = ('first_name','last_name','contact','gender','email','password1','password2')
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'First Name'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Last Name'}),
      'contact': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder': 'Contact Number'}),
      'email': forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'Email'}),
      'gender' : forms.RadioSelect(attrs={'class': 'form-control form-control-user'}),
    }


class ProfileForm(forms.ModelForm):
    
  def __init__(self, *args, **kwargs):
    super(ProfileForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_show_labels = False 
  
  class Meta:
    
    model = MyUser
    fields = ('profile_pic','first_name','last_name','contact','email')
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'First Name'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control form-control-user','placeholder': 'Last Name'}),
      'contact': forms.NumberInput(attrs={'class': 'form-control form-control-user','placeholder': 'Contact'}),
      'email': forms.EmailInput(attrs={'class': 'form-control form-control-user','placeholder': 'Email'}),
    }