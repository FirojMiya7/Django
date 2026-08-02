from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse


from django.shortcuts import render
from .models import todo

# def home(request):
#     context = {
#         'username': "Hulk",
#     }
#     return render(request, 'blog/home.html', context)

# def about(request):
#     return render(request, 'blog/about.html')

# def blog_detail(request, id):
#     context = {
#         'id': id
#     }
#     return render(request, 'blog/blog_detail.html', context)

# def blog_list(request):
#     posts = ['First Post','Second Post','Third Post']
#     context = {
#         'posts': posts
#     }
#     return render(request, 'blog/blog_list.html', context)


def mainHome(request):
    todoData = todo.objects.all()
    return render(request, 'blog/mainHome.html', {'data': todoData})


def home(request):
    todoData = todo.objects.all()
    return render(request, 'blog/home.html', {'data': todoData})


def details(request, id):
    taskData = get_object_or_404(todo, pk=id)
    print(taskData.taskDescription)
    return render(request, 'blog/detail.html', {'todo': taskData})