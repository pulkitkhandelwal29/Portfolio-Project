from django.urls import path

#importing views.py of the Blog app (as it is in the current directory)
from . import views

#calling the function allblogs in views.py file
urlpatterns = [
    path('',views.allblogs, name='allblogs'),
    #will look for blog_id and it should be int
    path('<int:blog_id>/',views.detail, name='detail'),
]
