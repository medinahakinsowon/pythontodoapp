from django.contrib import admin
from . models import TaskTodo

# Register your models here.

class TaskTodoAdmin(admin.ModelAdmin):
  list_display = ('task', 'is_completed', 'updated_at')
  search_fields = ('task',)

admin.site.register(TaskTodo, TaskTodoAdmin)
