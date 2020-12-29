from django.urls import path
from .views import home, todo_create, todo_update, todo_delete,list

urlpatterns = [
   
  
    path('', home, name = 'home'),
    path('list/', list, name = 'list'),
    path('create/',todo_create, name = 'create'),
    path('<int:id>/delete/',todo_delete, name = 'delete'),
    path('<int:id>/update/', todo_update, name = 'update'),
]
