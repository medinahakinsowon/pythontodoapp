from django.http import HttpResponse
from django.shortcuts import render
from todoapp.models import TaskTodo


def home(request):
  tasks = TaskTodo.objects.filter(is_completed=False).order_by('-updated_at')
  context = {
    'tasks': tasks
  }
  return render(request, 'home.html', context)