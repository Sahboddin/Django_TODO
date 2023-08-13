from django.contrib import admin
from .models import TaskModel
# Register your models here.
class task_register(admin.ModelAdmin):
    list_display = ('taskTitle','taskDescription','is_completed')  
admin.site.register(TaskModel,task_register)      