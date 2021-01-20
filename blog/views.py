#"get_object_or_404" helps to get the object and if no object is there, returns 404 error
from django.shortcuts import render,get_object_or_404

from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request,'blog/allblogs.html',{'blogs':blogs})

def detail(request,blog_id):
    #"get_object_or_404" takes parameters as the (model name, and the primary key from where the value will be retrieved)
    detailblog=get_object_or_404(Blog, pk=blog_id)
    return render(request,'blog/detail.html',{'blog':detailblog})
