from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def login_user(request):
    if request.method =="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Login failed. Please try again.")
            # Render the login page with the error message
            return render(request, 'registration/login.html', {'message': 'Login failed. Please try again.'})


    else:
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out.")
    return render(request, 'main.html', {'message' : "You were logged out."})