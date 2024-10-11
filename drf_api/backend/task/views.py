from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET', 'POST'])
def tasks(request):
    completed_params = request.query_params.get('completed', None)

    tasks = get_filtered_tasks(completed_params)

    if tasks is None:
        return Response({'error': 'Invalid value for "completed". Use true or false.'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not tasks.exists():
        return Response({'message': 'No tasks available.'}, status=status.HTTP_200_OK)

    if request.method == 'GET':
        paginator = TaskPagination()
        paginated_tasks = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(paginated_tasks, many=True)
        return paginator.get_paginated_response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

def get_filtered_tasks(completed_params):
    if completed_params is not None:
        if completed_params.lower() == 'true':
            return Task.objects.filter(completed=True)
        elif completed_params.lower() == 'false':
            return Task.objects.filter(completed=False)
        else:
            return None
    else:
        return Task.objects.all()
    
class TaskPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@api_view(['GET', 'PUT', 'DELETE'])
def task_details(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response({'message': 'Task deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['PATCH'])
def mark_task_completed(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':   
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated succesfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    