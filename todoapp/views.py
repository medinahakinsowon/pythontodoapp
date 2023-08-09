from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from . models import TaskTodo

# Create your views here. these are backend logics

def addTask(request):
  task = request.POST['task']
  TaskTodo.objects.create(task=task)
  return redirect( 'home')

def mark_task_as_done(request, pk):
  task = get_object_or_404(TaskTodo, pk=pk)
  task.is_completed = True
  task.save()
  return redirect('home')

def mark_as_undone(request, pk):
   task = get_object_or_404(TaskTodo, pk=pk)
   task.is_completed = False
   task.save()
   return redirect('home')
 
def edit_task(request, pk):
  get_task = get_object_or_404(TaskTodo, pk=pk)
  if request.method == 'POST':
    new_task = request.POST['task']
    get_task.task = new_task
    get_task.save()
    return redirect('home')
  else:
    context = {
      'get_task': get_task,
    }
    return render(request, 'edit_task.html', context)


def delete_task(request, pk):
  task = get_object_or_404(TaskTodo, pk=pk)
  task.delete()
  return redirect('home')