
from django.contrib import admin

# "include" helps to include the urls.py of the other app
from django.urls import path,include

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files
from django.conf.urls.static import static

#importing views from the models for homepage
import jobs.views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',jobs.views.home, name='home'),
    path('blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

#This blog is like receving the request from the user for blog, then the request is forwarded to the
#urls.py of the blog app and then it responds accordingly
