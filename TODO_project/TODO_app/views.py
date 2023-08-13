from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel
# Create your views here.
def home(request):
    data = TaskModel.objects.all()
    return render(request,'show_task.html', {'data' : data})

def edit_t(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_task')
        
    else:
        form=TaskForm()
    return render(request,'edit_task.html',{'form' : form})

def complete_t(request):
    data = TaskModel.objects.all() 
    return render(request,'complete_task.html',{'data' : data})

def delete(request,id):
    TaskModel.objects.get(pk=id).delete()
    return redirect('show_task')

def edit(request,id):
    data = TaskModel.objects.get(pk=id)
    form = TaskForm(instance=data)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('show_task')
    return render(request,'edit_task.html',{'form' : form})
        
def complete(request,id):
    com_data = TaskModel.objects.get(pk=id)
    com_data.is_completed = True
    com_data.save()
    return redirect('complete_task')
