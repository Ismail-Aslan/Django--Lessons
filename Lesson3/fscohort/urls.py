from django.urls import path,include

from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
]
