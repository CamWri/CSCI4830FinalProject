from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User  # Corrected import
from .models import CoreSubject, Course
from django.shortcuts import render, get_object_or_404
from .models import User, Ticket

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
    template = loader.get_template('main.html')
    return HttpResponse(template.render())