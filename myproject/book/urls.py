from django.urls import path
from . import views
urlpatterns = [
    path('', views.book_list, name='book'),
    path('detail/<int:id>/',views.Book_detail, name='book_detail'),
    path('add/', views.Book_create, name='book_create'),
    path('update/<int:id>/', views.Book_update, name='book_update'),
    path('delete/<int:id>/', views.Book_delete, name='book_delete'),
]
