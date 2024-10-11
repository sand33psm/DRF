from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @action(detail=True, methods=['post'])
    def mark_completed(self, request, pk=None):
        task = self.get_object()
        task.completed = True
        task.save()

        return Response({'status': 'Task marked as completed.'})
    
    @action(detail=False, methods=['get'])
    def completed_tasks(self, request):
        tasks = Task.objects.filter(completed=True)
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)


# class TaskList(mixins.CreateModelMixin,
#                mixins.ListModelMixin,
#                generics.GenericAPIView):
    
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# tasklist = TaskList.as_view()  


# class TaskDetails(mixins.RetrieveModelMixin, 
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   generics.GenericAPIView):
    
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# task_details = TaskDetails.as_view()

# ---------------------------------------------------------------------------- #

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# tasklist = TaskList.as_view()   

# class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# task_details = TaskDetails.as_view()




# ================================================================== # 

# class TaskList(APIView):
#     def get(self, request):
#         tasks = Task.objects.all()
#         if not tasks:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = TaskSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response({'error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

# tasklist = TaskList.as_view()


# class TaskDetails(APIView):
#     def get(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         if not task:
#             return Response({'error': 'Task not found!'})

#         serializer = TaskSerializer(task)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        

#     def put(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         serializer = TaskSerializer(task,   data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Something went wrong!'}, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         task = get_object_or_404(Task, pk=pk)
#         task.delete()
#         return Response({'message': 'Task deleted succesfully'}, status=status.HTTP_200_OK)

# task_details = TaskDetails.as_view()
# ---------------------------------------------------------------- #

# class TaskList(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# tasklist = TaskList.as_view()


# class TaskDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

# task_details = TaskDetails.as_view()

