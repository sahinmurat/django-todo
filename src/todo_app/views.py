from .forms import TodoAddForm, TodoUpdateForm
from django.shortcuts import get_object_or_404, redirect, render
from .models import Todo

# Create your views here.

def home(request):
    return render(request, 'todo_app/home.html')

def list(request):
    todo = Todo.objects.all()
    context = {
        'todo': todo
    }
    return render(request, 'todo_app/todo_list.html', context)
    
def todo_create(request):
    form = TodoAddForm()
    if(request.method == 'POST' ):
        form= TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
            'form' : form 
        }
    return render(request, 'todo_app/todo_create.html', context )
        


def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id)
    form = TodoUpdateForm(instance=todo)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    context= {
        'form': form
    }
    return render(request, 'todo_app/todo_update.html', context)

def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.delete()
        return redirect('list')
    context = {
        'todo':todo
    }
    return render(request,'todo_app/todo_delete.html', context)
