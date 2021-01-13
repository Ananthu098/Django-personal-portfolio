from django.shortcuts import render,get_object_or_404
from .models import blog

# Create your views here.
def all_blogs(request):
    return render(request,'blog/home.html',{'blo':blog.objects.order_by('-date')})
def detail(request,blog_id):
    data=get_object_or_404(blog,id=blog_id)
    return render(request,'blog/detail.html',{'blo':data})
