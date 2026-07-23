from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/<int:id>/', views.blog_detail, name='blog_detail'),
    path('blog/', views.blog_list, name='blog_list')
]