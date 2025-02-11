from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse
# Create your views here.


def view_todos(request):
    if request.user.is_authenticated:
        todos = Todo.objects.all().order_by("-id")
        context = {
            "todos": todos
        }
        return render(request, "home/index.html", context)
    else:
        return redirect("login")


def create_todo(request):
    if request.method =="POST": 
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo = Todo.objects.create(title=title, description=description)
        return redirect("home")
    return render(request, "home/index.html")


def complete_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
        todo.is_completed = True
        todo.save() 
    except :
        return HttpResponse("Todo not found, Invalid ID")
    
    return redirect("home")


def delete_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
        todo.delete()
    except:
        return HttpResponse("Todo not found, Invalid ID")
    return redirect("home")


def update_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
    except:
        return HttpResponse("Todo not found, Invalid ID")
    
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        todo.title = title
        todo.description = description
        todo.save()
        return redirect("home")


    return render(request, "home/update.html", {"todo": todo})
