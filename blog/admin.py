from django.contrib import admin

# Referring to current directory i.e. blog import from its models.py the class name
from .models import Blog

#register the class to get it appeared on the admin page.
#If u do not want any model to appear on Admin Page, then don't register here
#By registering Blog will appear on admin Page
admin.site.register(Blog)
