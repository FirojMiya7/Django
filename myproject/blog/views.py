from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    context = {
        'username': "Hulk",
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def blog_detail(request, id):
    context = {
        'id': id
    }
    return render(request, 'blog/blog_detail.html', context)

def blog_list(request):
    posts = ['First Post','Second Post','Third Post']
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_list.html', context)