from django.urls import path
from django.views.generic.base import TemplateView
from users.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # path('signup',UserSignup.as_view(template_name='auth/signup.html'),name='business-signup'),
    path('business/signup',bregister,name='business-signup'),
    path('business/login', blogin,name = 'business-login'),
    path('business/profile',BusinessProfileView.as_view(),name='profile'),
    path('business/profile-update/<pk>', ProfileUpdateView.as_view(),name = 'profile-update'),
    
    path('user/signup',uregister,name='user-signup'),
    path('user/login',ulogin,name='user-login'),
    
    path('user/logout',userlogout,name='user-logout'),
]