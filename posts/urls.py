from django.urls import path
from . import views
from .views import account, delete_account


urlpatterns = [
    path('', views.main, name = 'main'),
    path('users/', views.users, name='users'),  
    path('users/userDetails/<int:user_id>/', views.userDetails, name="User Details"),
    path('subjects/', views.subjects, name = 'subjects'),
    path('subjects/subjectDetails/<str:subject>', views.subjectDetails, name = "Subject Details"),
    path('subjects/subjectDetails/<str:subject>/<str:course_name>/', views.courseDetails, name='course_details'),
    path('subjects/subjectDetails/<int:ticket_id>/', views.ticket, name='ticket'),
    path('media/', views.courseDetails, name='course_details'),
    path('account/', views.account, name = "account" ),
    path('add_post/', views.add_post, name = "add_post"),
    path('search_tickets/', views.search_tickets, name = "search_tickets"),
    path('account/', account, name='account'),
    path('delete_account/', delete_account, name='delete_account'),
    path('requestedCourse/', views.add_SugguestCourse , name='requested_Course'),

    #get rid of this lines 6 and 7 eventually because we don't want them to see all users

    #I want a page where it is a list of all subjects(Core Subjects Page) where if clicked, it goes to a list of all possible
    #   courses for the subject
    #I then want a unique list of all classes from that subject so use something like line 7 but instead of 
    #    details about a user, it is a new page that is all the courses/classes possible for that subject
    #I then want for each course/class, when clicked, it goes to a new page that has all the posts where in each post
    #   it displays the user that post it(first and last), the post title(maybe) and post description, and then any video, 
    #   pdf, or url

    #Account page where you can see your username, first name, last name, password, email, maybe all posts, etc
    #   In this page, if you can see all your posts(minimzed version)
    #POsisble test urls in the future:

]
