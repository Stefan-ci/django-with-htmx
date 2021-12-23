from django.shortcuts import render
from todo.models import Todo
from django.http import HttpResponse
from django.contrib import messages


def delete_todo_view(request, pk):
    task = Todo.objects.get(pk=pk)
    task.delete()
    messages.success(request, f"Vous avez supprimé cette tâche!")
    return HttpResponse('')


def add_todo_view(request):
    name = request.POST['name']
    Todo.objects.create(name=name)
    messages.success(request, "La tâche a été ajoutée avec succès!")
    return HttpResponse('')


def home_view(request):
    tasks = Todo.objects.all().order_by('id')
    context = {
        'tasks': tasks,
    }
    return render(request, 'index.html', context)
