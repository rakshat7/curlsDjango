from unicodedata import name
from django.urls import path
from django.views.generic import TemplateView
from curls.views import *

urlpatterns = [
    path('',curls, name= 'curls'),
    path('user-dashboard',userpage, name= 'user-dashboard'),
    path('business-detail/<int:b_id>',business_detail, name= 'business-detail'),
    path('book-appointment/<int:b_id>',bookapp, name= 'bookappointment'),
]