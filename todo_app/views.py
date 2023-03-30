from django.shortcuts import render,redirect
from .models import task
from .forms import todoform
from django.views.generic import ListView
from django.views.generic.detail import DetailView


class TaskListView(ListView):
    model=task
    template_name='home.html'
    context_object_name='task1'
class TaskDetailView(DetailView):
    model=task
    template_name='details.html'
    context_object_name='task1'    


# Create your views here.
def index(request):
    object=task.objects.all()
    if request.method=='POST':
        taskname=request.POST.get('taskname')
        priority=request.POST.get('priority')
        date=request.POST.get('date')
        todo=task(task=taskname,priority=priority,date=date,time=None)
        todo.save()
    return render(request,'index.html',{'tasks':object})

def delete(request,id):
    if request.method=='POST':
        object=task.objects.get(id=id)
        object.delete()
        return redirect('/')   
    return render(request,'delete.html')    

def update(request,id):
    object=task.objects.get(id=id)
    f=todoform(request.POST or None, instance=object)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})    

 