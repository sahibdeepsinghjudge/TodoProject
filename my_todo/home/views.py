from django.shortcuts import render, redirect
from .models import Todo
from django.http import HttpResponse
# Create your views here.


def view_todos(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(created_by=request.user).order_by("-id")
        print(request.user)

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
        todo = Todo.objects.create(title=title, description=description,created_by=request.user)
        return redirect("home")
    return render(request, "home/index.html")


def complete_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if todo.created_by == request.user:
            todo.is_completed = True
            todo.save() 
        else:
            return HttpResponse("You are not authorized to complete this todo")
    except :
        return HttpResponse("Todo not found, Invalid ID")
    
    return redirect("home")


def delete_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if todo.created_by == request.user:
            todo.delete()
        else:
            return HttpResponse("You are not authorized to delete this todo")
    except:
        return HttpResponse("Todo not found, Invalid ID")
    return redirect("home")


def update_todo(request,id):
    try:
        todo = Todo.objects.get(id=id)
        if todo.created_by != request.user:
            return HttpResponse("You are not authorized to update this todo")

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
