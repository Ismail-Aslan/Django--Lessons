from django.shortcuts import render
from django.http import HttpResponse
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def home(request):
    return HttpResponse('<center><h1>Welcome to apiTodo</h1></center>')


@api_view(['GET'])
def todoList(request):
    queryset = Todo.objects.all()
    
    serializer = TodoSerializer(queryset,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def todoListCreate(request):
    serializer = TodoSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)