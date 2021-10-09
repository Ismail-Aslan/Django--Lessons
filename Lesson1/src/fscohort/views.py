from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("<h1> Hello World...</h1>")
def home2(request):
    return HttpResponse("<h1> Hello World 2...</h1>")