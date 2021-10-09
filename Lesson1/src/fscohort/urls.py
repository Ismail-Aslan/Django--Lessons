from django.contrib import admin
from django.urls import path
from fscohort.views import home2

urlpatterns = [
    path('home/', home2),
]
