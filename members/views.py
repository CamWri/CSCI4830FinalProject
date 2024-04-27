from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm

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
            isAuthenticated = request.user.is_authenticated
            ticketlist = Ticket.objects.all()
            random_tickets = random.sample(list(ticketlist), min(len(ticketlist), 5)) # Select up to 5 random tickets
            mysubjects = CoreSubject.objects.all().values()
            template = loader.get_template('main.html')
            context = {
                'mysubjects': mysubjects,
                'ticketlist': random_tickets,
                'isAuthenticated' : isAuthenticated,
            }
            return HttpResponse(template.render(context, request))
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})

def account(request):
    isAuthenticated = request.user.is_authenticated
    # Check if the user is logged in
    if request.user.is_authenticated:
        # User is logged in, you can access account details
        user = request.user
        # Access user attributes to get account details
        username = user.username
        email = user.email
        # You can access any other fields of the user model as needed

        # Pass account details to the template
        context = {
            'username': username,
            'email': email,
            'isAuthenticated' : isAuthenticated,
            # Add more fields as needed
        }
        # Render the template with account details
        return render(request, 'account.html', context)
    else:
        # User is not logged in, you can handle this case as needed
        # For example, redirect to login page
        return HttpResponse("You are not logged in.")
# branch created to merge with main