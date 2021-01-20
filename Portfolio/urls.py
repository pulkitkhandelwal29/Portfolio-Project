
from django.contrib import admin
from django.urls import path

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files
from django.conf.urls.static import static

#importing views from the models for homepage
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home')
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
