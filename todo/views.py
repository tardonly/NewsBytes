from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth import logout
from django.contrib.auth.views import logout
from .models import Todo
from .forms import TodoForm
@login_required
def index(request):
    todo_list1 = [todo for todo in Todo.objects.order_by('id') if (todo.creator==request.user.username and todo.complete==True) ]
    todo_list2 = [todo for todo in Todo.objects.order_by('id') if (todo.buddy==request.user.username and todo.complete!=True) ]
    todo_list = todo_list1+todo_list2
    form = TodoForm()
    current_user = request.user.username
    try:
        error = request.session['error']
    except Exception as e:
        error = ""
    context = {'todo_list' : todo_list, 'form' : form,'error':error,'current_user':current_user}
    request.session['error']=""
    return render(request, 'todo/index.html', context)

@require_POST
def addTodo(request):
    error=""
    form = TodoForm(request.POST)
    usernames = [i.username for i in User.objects.all() if i.username!=request.user.username]
    if form.is_valid():
        buddy=request.POST['username']
        if buddy in usernames:        
            new_todo = Todo(text=request.POST['text'],buddy=buddy,creator=request.user.username)
            new_todo.save()
        else:
            error = "buddy not found"
    request.session['error']=error
    return redirect('index')

def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteAll(request):
    Todo.objects.all().delete()

    return redirect('index')
