from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
#from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponse

from django.template import loader
import random

from posts.models import CoreSubject, Ticket


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
    return render(request, 'logout.html', {'message' : "You were logged out."})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Save the form and retrieve the saved user
            user = form.save()
            # Optionally, you can log in the user after registration
            # authenticate user before login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            # Redirect to the login page
            ticketlist = Ticket.objects.all()
            random_tickets = random.sample(list(ticketlist), min(len(ticketlist), 5)) # Select up to 5 random tickets
            mysubjects = CoreSubject.objects.all().values()
            template = loader.get_template('main.html')
            context = {
                'mysubjects': mysubjects,
                'ticketlist': random_tickets,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})


# branch created to merge with main