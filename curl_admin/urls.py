from unicodedata import name
from django.urls import path
from django.views.generic.base import TemplateView
from .views import *
from django.contrib.auth.decorators import login_required
from users.decorators import allowed_users

urlpatterns = [
    path('dashboard',dashboard,name='dashboard'),
    
    path('business',BusinessListView.as_view(),name='business'),
    path('register-business',RegisterBusiness.as_view(),name='register-customer'),
    path('update-business/<pk>',BusinessUpdateView.as_view(),name='update-business'),
    path('delete-business/<pk>',BusinessDeleteView.as_view(),name='delete-business'),
    
    path('b-hour',BhourListView.as_view(),name='b-hour'),
    path('add-b-hour',AddBhour.as_view(),name='add-b-hour'),
    path('update-b-hour/<pk>',BhourUpdateView.as_view(),name='update-b-hour'),
    path('delete-b-hour/<pk>',BhourDeleteView.as_view(),name='delete-b-hour'),
    
    path('add-customer',AddCustomer.as_view(),name='add-customer'),
    path('customers',CustomerListView.as_view(),name='customers'),
    path('update-customer/<pk>',CustomerUpdateView.as_view(),name='update-customer'),
    
    path('book-appointment/<int:cust_id>',bookapp,name='book-appointment'),
    path('appointments',AppointmentListView.as_view(),name='appointments'),
    path('cancel-appointment/<pk>',AppointmentDeleteView.as_view(),name='cancel-appointment'),
    path('update-appointment/<pk>',AppointmentUpdateView.as_view(),name='update-appointment'),
    
    path('add-service',AddServiceView.as_view(),name='add-service'),
    path('services',ServicesListView.as_view(),name='services'),
    path('update-service/<pk>',ServiceUpdateView.as_view(),name='update-service'),
    path('delete-service/<pk>',ServiceDeleteView.as_view(),name='delete-service'),
    
    path('add-dept',AddDepartmentView.as_view(),name='add-dept'),
    
    path('add-emp',AddEmployeeView.as_view(),name='add-emp'),
    path('employees',EmployeesListView.as_view(),name='employees'),
    path('update-emp/<pk>',EmployeeUpdateView.as_view(),name='update-emp'),
    path('delete-emp/<pk>',EmployeeDeleteView.as_view(),name='delete-emp'),
    
    path('checkout/<int:id>',checkout),
    path('charge',charge,name="charge")
]
