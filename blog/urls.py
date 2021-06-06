from django.urls import path

#importing views.py of the Blog app (as it is in the current directory)
from . import views

#calling the function allblogs in views.py file
urlpatterns = [
    #Separate homepage for blogs app (It means whenever anyone will come to blog, it will show this page)
    path('',views.allblogs, name='allblogs'),
    #will look for blog_id and it should be int (it is for looking each blog separately when we click on it)
    #Whenever someone will write /blog/1, it will see it is an integer and assign it to blog_id which in turn will go to views.detail function 
    path('<int:blog_id>/',views.detail, name='detail'),
]
