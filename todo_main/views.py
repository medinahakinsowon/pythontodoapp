from django.http import HttpResponse
from django.shortcuts import render
from todoapp.models import TaskTodo


def home(request):
  tasks = TaskTodo.objects.filter(is_completed=False).order_by('-updated_at')
  
  completed_task = TaskTodo.objects.filter(is_completed=True).order_by('-updated_at')

  context = {
    'tasks': tasks,
    'completed_task': completed_task,
  }
  return render(request, 'home.html', context)