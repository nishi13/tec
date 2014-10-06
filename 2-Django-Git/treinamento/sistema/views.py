from django.shortcuts import render
from sistema.models import *
from sistema.forms import *

# Create your views here.


def home(request):
    todo_list = Todo.objects.all()
    todo_form = TodoForm()
    if request.method == 'POST':
        todo_form = TodoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
    return render(request, 'home.html', locals())
