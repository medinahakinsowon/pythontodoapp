from django.shortcuts import  redirect,render
from django.http import HttpResponse
from . models import TaskTodo

# Create your views here.

def addTask(request):
  task = request.POST['task']
  TaskTodo.objects.create(task=task)
  return redirect( 'home')
