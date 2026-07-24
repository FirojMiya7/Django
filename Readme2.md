TOPIC 6: TEMPLATE TAGS, FILTERS & TEMPLATE INHERITANCE

THEORY
------
Problem: repeating <html><head><body> in every template is bad practice.
Solution: Template Inheritance -> one base.html, others extend it.

KEY TAGS
{% block name %} {% endblock %}   -> defines overridable section in base
{% extends 'template.html' %}     -> child template inherits from base

COMMON TAGS
{% if %} {% endif %}       -> conditional
{% for %} {% endfor %}     -> loop
{% empty %}                -> fallback content if loop list is empty
{% url 'name' %}           -> generate URL by its name (not hardcoded)

FILTERS (use | after variable)
upper     -> uppercase              {{ name|upper }}
lower     -> lowercase              {{ name|lower }}
length    -> count items            {{ posts|length }}
date      -> format date            {{ post.date|date:"D, d M Y" }}
default   -> fallback if empty       {{ value|default:"N/A" }}

CODE

1) blog/templates/blog/base.html
------------------------------------
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Blog{% endblock %}</title>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a> |
        <a href="{% url 'about' %}">About</a>
    </nav>
    <hr>

    {% block content %}
    {% endblock %}

    <hr>
    <footer>
        <p>&copy; 2026 My Django Blog</p>
    </footer>
</body>
</html>

2) blog/templates/blog/home.html
------------------------------------
{% extends 'blog/base.html' %}
{% block title %}Home Page{% endblock %}
{% block content %}
    <h1>Welcome, {{ username|upper }}!</h1>
    <p>This is the home page rendered using a template.</p>
{% endblock %}

3) blog/templates/blog/about.html
------------------------------------
{% extends 'blog/base.html' %}
{% block title %}About Page{% endblock %}
{% block content %}
    <h1>About Us</h1>
    <p>This is the about page.</p>
{% endblock %}

4) blog/templates/blog/blog_detail.html
-------------------------------------------
{% extends 'blog/base.html' %}
{% block title %}Blog Post {{ id }}{% endblock %}
{% block content %}
    <h1>Blog Post #{{ id }}</h1>
    <p>This is the detail page for blog post number {{ id }}.</p>
{% endblock %}

5) blog/templates/blog/blog_list.html
-----------------------------------------
{% extends 'blog/base.html' %}
{% block title %}All Posts{% endblock %}
{% block content %}
    <h1>All Blog Posts ({{ posts|length }})</h1>
    <ul>
        {% for post in posts %}
            <li>{{ post }}</li>
        {% empty %}
            <li>No posts available.</li>
        {% endfor %}
    </ul>
{% endblock %}

6) blog/views.py
------------------
from django.shortcuts import render

def home(request):
    context = {'username': 'krishna'}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def blog_detail(request, id):
    context = {'id': id}
    return render(request, 'blog/blog_detail.html', context)

def blog_list(request):
    posts = ['First Post', 'Second Post', 'Third Post']
    context = {'posts': posts}
    return render(request, 'blog/blog_list.html', context)

7) blog/urls.py
------------------
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog-list/', views.blog_list, name='blog_list'),
]

TEST
-----
python manage.py runserver
/blog-list/  -> shows list of 3 posts with count in heading