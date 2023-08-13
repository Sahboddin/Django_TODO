from django import forms
from .models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = '__all__'
    # labels = {
    #     'taskTitle' : 'Title',
    #     'taskDescription' : 'Description',
    #     'is_completed' : 'Status'
    # }