from django.urls import path
from . import views

urlpatterns = [
    path('', views.booklist, name='booklist'),
    path('book_details/<int:pk>/', views.book_details, name='book_details'),
]
