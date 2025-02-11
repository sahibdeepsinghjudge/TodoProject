from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
# Create your views here.


def create_account(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        # for user in User.objects.all():
        #     if user.email == email:
        #         return HttpResponse("Email already exists")
        #     if user.username == username:
        #         return HttpResponse("Username already exists")


        if email in User.objects.values_list("email", flat=True):
            return HttpResponse("Email already exists")
        if username in User.objects.values_list("username", flat=True):
            return HttpResponse("Username already exists")
        
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        print("User created")
        return redirect("login")

    return render(request, "accounts/create_account.html")



def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # login to handle login of user will come here
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth_login(request,user)
            return redirect("home")
        else:
            return HttpResponse("Invalid credentials")    

    return render(request, "accounts/login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")