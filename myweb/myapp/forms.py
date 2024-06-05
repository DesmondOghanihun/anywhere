from django import forms
from .models import Contact, ICTTrainingRequest, ICTRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'id': 'message'}),
        }

class ICTTrainingRequestForm(forms.ModelForm):
    class Meta:
        model = ICTTrainingRequest
        fields = ['name', 'course', 'email', 'phone', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Location'}),
        }
        labels = {
            'name': 'Full Name',
            'course': 'Course Name',
            'email': 'Email Address',
            'phone': 'Phone Number',
            'location': 'Location',
        }

class ICTRequestForm(forms.ModelForm):
    class Meta:
        model = ICTRequest
        fields = ['name', 'course', 'email', 'phone', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Course of Interest'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Phone/WhatsApp Number'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}),
        }
        labels = {
            'name': 'Name',
            'course': 'Course of Interest',
            'email': 'Email',
            'phone': 'Contact Phone/WhatsApp Number',
            'location': 'Location',
        }
