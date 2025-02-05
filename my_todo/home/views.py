from django.shortcuts import render, redirect
from .models import Todo
# Create your views here.


def view_todos(request):
    todos = Todo.objects.all().order_by("-id")
    context = {
        "todos": todos
    }
    return render(request, "home/index.html", context)


def create_todo(request):
    if request.method =="POST": 
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo = Todo.objects.create(title=title, description=description)
        return redirect("home")
    return render(request, "home/index.html")

     