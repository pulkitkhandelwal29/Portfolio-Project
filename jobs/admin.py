from django.contrib import admin

# Referring to current directory i.e. jobs, import from its models.py the class name
from .models import Job

#register the class to get it appeared on the admin page.
#If u do not want any model to appear on Admin Page, then don't register here
#By registering Jobs will appear on admin Page
admin.site.register(Job)
