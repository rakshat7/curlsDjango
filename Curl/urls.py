from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from curl_admin.views import *
from users.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',include('curls.urls')),
    path('admin/',include('curl_admin.urls')),
    path('', include('users.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
