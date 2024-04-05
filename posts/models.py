from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class Ticket(models.Model):
    user = models.ForeignKey(User, blank = True, null = True, on_delete = models.PROTECT)
    title = models.CharField("Title", max_length = 100)
    time_of_post = models.DateTimeField("Time of Post")
    post_description = models.CharField("Description", max_length = 500, null = True)
    pdf_file = models.FileField('PDF File', null = True, blank = True, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc'])])
    video_file = models.FileField('Video File', null = True, blank = True, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    video_website_address = models.URLField('Video Adress', null = True, blank = True)

    def __str__(self):
        return f"{self.user} {self.title} {self.post_description}"
    
class Course(models.Model):
    course_name = models.CharField("Course", max_length = 75)
    all_tickets = models.ManyToManyField(Ticket, null = True, blank=True)

    def __str__(self):
        return f" {self.course_name}"
    
class CoreSubject(models.Model):
    subject = models.CharField("Core Subject", max_length = 75)
    courses = models.ManyToManyField(Course, null = True, blank = True)

    def __str__(self):
        return f" {self.subject}"