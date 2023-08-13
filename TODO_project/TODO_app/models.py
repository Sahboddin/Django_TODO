from django.db import models

# Create your models here.
class TaskModel(models.Model):
    id = models.IntegerField(primary_key=True)
    taskTitle = models.CharField(max_length=150)
    taskDescription = models.CharField(max_length=300)
    is_completed = models.BooleanField(default= False)