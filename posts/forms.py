from django import forms
from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):  # Corrected class name
    class Meta:
        model = Ticket
        fields = ('title', 'time_of_post', 'post_description', 'video_website_address','pdf_file', 'video_file')

        labels = {
            'title': '',
            'time_of_post': '',
            'post_description': '',
            'pdf_file': 'PDF File',
            'video_file': 'MP4 File',
            'video_website_address': ''
        }

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 600px; margin: auto;', 'placeholder': 'Input your posts title'}),  # Example width: 300px
            'time_of_post': forms.DateTimeInput(attrs={'class': 'form-control', 'style': 'width: 600px; margin: auto', 'placeholder': 'Year-Month-Day Hour:Minute:Sec'}),  # Example width: 200px
            'post_description': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 600px; margin: auto', 'placeholder': 'Input Post Description'}),  # Example width: 400px
            'video_website_address': forms.URLInput(attrs={'class': 'form-control', 'style': 'width: 600px; margin: auto', 'placeholder': 'Input Video URL'}),  # Example width: 200px
            'pdf_file': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 200px; margin: auto; border: none; display: inline;', 'placeholder': ''}),  # Example width: 200px
            'video_file': forms.FileInput(attrs={'class': 'form-control', 'style': 'width: 200px; margin: auto; border: none; display: inline;', 'placeholder': ''}),  # Example width: 200px
        }


    