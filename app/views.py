from django.shortcuts import render
from . models import Gallery,Blog,Services



def index(request):
    img = Gallery.objects.all()
    blog = Blog.objects.all()
    services = Services.objects.all()
    context = {
        'img':img,
        'blog':blog,
        'services':services
        }
    return render(request,'index.html',context=context)


def about(request):
    return render(request,'about.html')


def faq(request):
    return render(request,'faq.html')


def blog(request,pk):
    blog = Blog.objects.get(id=pk)

    context = {
        'blog':blog
    }
    return render(request,'blog.html',context=context)


def gallery(request):
    img = Gallery.objects.all()
    context = {
        'img':img
    }
    return render(request,'gallery.html',context = context)


def services(request,pk):
    data = Services.objects.get(id=pk)

    context = {
        'data':data
    }
    
    return render(request,'services.html',context=context)