from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<center><h1>Welcome to apiTodo</h1></center>')
