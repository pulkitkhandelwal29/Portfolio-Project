from django.shortcuts import render

#Importing job class from models.py of Jobs app
#It is called so that we can import what we have in database and render it to the html page for displaying
from .models import Job

def home(request):
    #It is calling all the objects i.e. database from the Job class
    jobs = Job.objects
    return render(request,'jobs/home.html',{'jobs':jobs})
