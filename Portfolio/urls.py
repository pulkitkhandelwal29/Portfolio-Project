
from django.contrib import admin

# "include" helps to include the urls.py of the other app
from django.urls import path,include

#This is the settings.py containing information about the MEDIA_URL and MEDIA_ROOT
from django.conf import settings

#Helps to work with the static files (Here it is used to add static files taht are present in Media Folder )
from django.conf.urls.static import static

#importing views from the models for homepage
import jobs.views



urlpatterns = [
    path('admin/', admin.site.urls),
    #For homepage, go to jobs.views file and execute home function
    path('',jobs.views.home, name='home'),
    #If Blog request is generated, go to particular app "urls.py" file (need to create urls.py file there)
    path('blog/',include('blog.urls')),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)

#We need to add static class to let django know that we need to access the Media URL and Media root that we defined in settings.py

#This blog is like receving the request from the user for blog, then the request is forwarded to the
#urls.py of the blog app and then it responds accordingly
