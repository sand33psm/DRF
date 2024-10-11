from django.shortcuts import render
from rest_framework import generics # type: ignore
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateApi):
    queryset = BlogPost.objects.all()
    serializer_class =  BlogPostSerializer
