from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User  # Corrected import
from .models import CoreSubject, Course, Ticket
from django.shortcuts import render, get_object_or_404
import random

from django.contrib.auth import logout
from django.shortcuts import redirect

from django.views.decorators.csrf import csrf_protect

from django.http import HttpResponseRedirect

from .forms import TicketForm, SugguestCourseForm

from django.contrib.auth.models import User

def users(request):
    myusers = User.objects.all().values()
    template = loader.get_template('all_users.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))

def userDetails(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    tickets = Ticket.objects.filter(user=user)
    return render(request, 'user_details.html', {'user': user, 'tickets': tickets})

def subjectDetails(request, subject):
    core_subject = CoreSubject.objects.get(subject=subject)
    courses = core_subject.courses.all()
    template = loader.get_template('subjects_details.html')
    context = {
        'subject': core_subject,
        'courses': courses,
    }
    return HttpResponse(template.render(context, request))

def subjects(request):
    mysubjects = CoreSubject.objects.all().values()
    template = loader.get_template('all_subjects.html')
    context = {
        'mysubjects': mysubjects,
    }
    return HttpResponse(template.render(context, request))

def courseDetails(request, subject, course_name):
    course = get_object_or_404(Course, course_name=course_name)
    ticket_list = course.all_tickets.all()
    template = loader.get_template('course.html')
    context = {
        'course': course,
        'ticket_list': ticket_list,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    ticketlist = Ticket.objects.all()
    random_tickets = random.sample(list(ticketlist), min(len(ticketlist), 5)) # Select up to 5 random tickets
    mysubjects = CoreSubject.objects.all().values()
    template = loader.get_template('main.html')
    context = {
        'mysubjects': mysubjects,
        'ticketlist': random_tickets,
    }
    return HttpResponse(template.render(context, request))


def account(request):
    template = loader.get_template('account.html')
    return HttpResponse(template.render())

def delete_account(request):
    return render('account')

def add_post(request):
    submitted = False
    template = 'add_post.html'

    if request.method == "POST":
        form = TicketForm(request.POST)
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
    }
    return render(request, template, context)


@csrf_protect
def search_tickets(request):
    template_name = 'search_tickets.html'  # Name of the template file

    if request.method == "POST":
        search_query = request.POST.get('search_query', '')  # Safely get the search query

        posts = Ticket.objects.filter(title__contains=search_query)

        context = {
            "search_query": search_query,
            "posts" : posts,
        }

        return render(request, template_name, context)
    else:
        context = {}  # If it's not a POST request, create an empty context
        return render(request, template_name, context)
    
def add_SugguestCourse(request):
    submitted = False
    template = 'requestedCourse.html'

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
    }
    return render(request, template, context)
