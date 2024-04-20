from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User  # Corrected import

from .models import CoreSubject, Course, SugguestCourse, Ticket

from django.shortcuts import render, get_object_or_404
import random

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponseRedirect

from .forms import TicketForm, SugguestCourseForm
from django.contrib.auth.models import User

def users(request):
    isAuthenticated = request.user.is_authenticated
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
        'isAuthenticated': isAuthenticated,
    }
    return HttpResponse(template.render(context, request))

def userDetails(request, user_id):
    isAuthenticated = request.user.is_authenticated
    user = get_object_or_404(User, pk=user_id)
    tickets = Ticket.objects.filter(user=user)
    return render(request, 'user_details.html', {'user': user, 'tickets': tickets, 'isAuthenticated': isAuthenticated,})

def subjectDetails(request, subject):
    isAuthenticated = request.user.is_authenticated
    core_subject = CoreSubject.objects.get(subject=subject)
    courses = core_subject.courses.all()
    template = loader.get_template('subjects_details.html')
    context = {
        'subject': core_subject,
        'courses': courses,
        'isAuthenticated': isAuthenticated,
    }
    return HttpResponse(template.render(context, request))

def subjects(request):
    isAuthenticated = request.user.is_authenticated
    mysubjects = CoreSubject.objects.all().values()
    template = loader.get_template('all_subjects.html')
    context = {
        'mysubjects': mysubjects,
        'isAuthenticated': isAuthenticated,
    }
    return HttpResponse(template.render(context, request))

def courseDetails(request, subject, course_name):
    isAuthenticated = request.user.is_authenticated
    course = get_object_or_404(Course, course_name=course_name)  
    core_subject = CoreSubject.objects.get(subject=subject)
    courses = core_subject.courses.all()
    mysubjects = CoreSubject.objects.all().values() 
    ticket_list = course.all_tickets.all()
    template = loader.get_template('course.html')
    context = {
        'mysubjects': mysubjects,
        'subject':core_subject,
        'course': course,
        'courses': courses,
        'ticket_list': ticket_list,
        'isAuthenticated': isAuthenticated,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    isAuthenticated = request.user.is_authenticated
    ticketlist = Ticket.objects.all()
    random_tickets = random.sample(list(ticketlist), min(len(ticketlist), 5)) # Select up to 5 random tickets
    mysubjects = CoreSubject.objects.all().values()
    template = loader.get_template('main.html')
    context = {
        'mysubjects': mysubjects,
        'ticketlist': random_tickets,
        'isAuthenticated': isAuthenticated,
    }
    return HttpResponse(template.render(context, request))


def delete_account(request):
    return render('account')

def add_post(request):
    submitted = False
    template = 'add_post.html'
    isAuthenticated = request.user.is_authenticated

    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)

            course_id = request.POST.get('ticket_course')

            # Convert the course ID to a Course object
            course = Course.objects.get(pk=course_id)

            ticket.save()

            # Add the ticket to the 'all_tickets' field of the course
            course.all_tickets.add(ticket)

            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = TicketForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'isAuthenticated': isAuthenticated,
    }
    return render(request, template, context)


@csrf_protect
def search_tickets(request):
    template_name = 'search_tickets.html'  # Name of the template file
    isAuthenticated = request.user.is_authenticated

    if request.method == "POST":
        search_query = request.POST.get('search_query', '')  # Safely get the search query

        posts = Ticket.objects.filter(title__contains=search_query)

        context = {
            "search_query": search_query,
            "posts" : posts,
            'isAuthenticated': isAuthenticated,
        }

        return render(request, template_name, context)
    else:
        context = {}  # If it's not a POST request, create an empty context
        return render(request, template_name, context)

def add_SugguestCourse(request):
    submitted = False
    template = 'requestedCourse.html'
    isAuthenticated = request.user.is_authenticated

    if request.method == "POST":
        form = SugguestCourseForm(request.POST)
        if form.is_valid():
            requestedCourse = form.save(commit=False)

            requestedCourse.save()

            return HttpResponseRedirect('/add_post?submitted=True')
    else:
        form = SugguestCourseForm()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        'isAuthenticated': isAuthenticated,
    }
    return render(request, template, context)

def ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    course_name = ticket.ticket_course
    isAuthenticated = request.user.is_authenticated
    context = {
        'ticket': ticket,
        'course_name': course_name,
        'isAuthenticated': isAuthenticated,
    }
    return render(request, 'ticket.html', context)

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