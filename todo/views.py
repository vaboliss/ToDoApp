from django.shortcuts import render, redirect
from .models import Todo
from django.views.decorators.http import require_POST
from .forms import TodoForm
# Create your views here.
@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    
    print(request.POST['text'])

    if form.is_valid():
        new_todo = Todo(text = form.cleaned_data['text'])
        new_todo.save()

    return redirect('index')

def index(request):

    form = TodoForm()
    todo_list = Todo.objects.order_by('id')
    context = { 'todo_list' : todo_list, 'form' : form}
    return render(request,'todo/index.html', context)

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.complete =True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')