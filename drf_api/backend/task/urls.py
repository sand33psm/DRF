from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('<int:pk>/', views.task_details, name='task_details'),
    path('mark_task_completed/<int:pk>/', views.mark_task_completed, name='mark_task_completed'),
    
]
