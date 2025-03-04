from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('books/new/', views.book_new, name='book_new'),
    path('books/<int:pk>/edit/', views.book_edit, name='book_edit'),
    path('books/<int:pk>/delete/', views.book_delete, name='book_delete'),
    path('books/register/', views.register, name='register'),
    path('books/login/', views.user_login, name='user_login'),
    path('books/logout/', views.user_logout, name='user_logout'),
]