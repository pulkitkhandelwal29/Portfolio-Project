
from django.contrib import admin
from django.urls import path

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
