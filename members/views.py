from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User
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

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            form.save()
            #get the new user info
            user = User.objects.get(username=uname)
            user.save()
            return redirect('/login')

        return redirect("/")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

# branch created to merge with main