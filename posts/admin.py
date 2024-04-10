from django.contrib import admin

from django.contrib import admin
from .models import Ticket
from .models import CoreSubject
from .models import Course

class TicketAdmin(admin.ModelAdmin):
    list_display = ("user","title", "post_description",)

class CoreSubjectAdmin(admin.ModelAdmin):
    list_display = ("subject",)

class CourseAdmin(admin.ModelAdmin):
    list_display = ("course_name",)

class SugguestCourseAdmin(admin.ModelAdmin):
    list_display = ("suggestedCourse",)


admin.site.register(Ticket, TicketAdmin)
admin.site.register(CoreSubject, CoreSubjectAdmin)
admin.site.register(Course, CourseAdmin)