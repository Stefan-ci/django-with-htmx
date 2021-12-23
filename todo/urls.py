from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('spprimer/la/tache/<int:pk>/', views.delete_todo_view, name='delete-task'),
    path('creer/une/nouvelle/tache/', views.add_todo_view, name='add-task'),
]
