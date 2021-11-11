from django.urls import  path
from .views import home,todoList,todoListCreate,todoListAll, todoListUpdate, todoListDelete,todoListDetail

urlpatterns = [
    path('', home),
    path('todoList/', todoList),
    path('todoListCreate/', todoListCreate),
    path('todoListAll/', todoListAll),
    path('todoListUpdate/<int:pk>/', todoListUpdate),
    path('todoListDelete/<int:pk>/', todoListDelete),
    path('todoListDetail/<int:pk>/', todoListDetail),
]