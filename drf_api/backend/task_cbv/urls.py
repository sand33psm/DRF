from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('', views.tasklist, name='tasklist'),    
    # path('task_details/<int:pk>/',views.task_details, name='task_details'),

]

