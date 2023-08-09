from django.urls import path
from . import views


urlpatterns = [
    #Add task
    path('addTask/', views.addTask, name="addTask"),
    #Mark as done
    path('mark_task_as_done/<int:pk>/', views.mark_task_as_done, name="mark_task_as_done"),
    # Mark as undone
    path('mark_as_undone/<int:pk>/', views.mark_as_undone, name="mark_as_undone"),
    #edit_task
    path('edit_task/<int:pk>/', views.edit_task, name="edit_task"),
    #delete_task
     path('delete_task/<int:pk>/', views.delete_task, name="delete_task"),
]
