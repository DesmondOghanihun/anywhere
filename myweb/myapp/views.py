from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ICTTrainingRequest, ICTRequest
from .forms import ContactForm, ICTRequestForm, ICTTrainingRequestForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contact form submitted successfully.")
    return HttpResponse("Invalid request method.")


def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')


def index(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def submit_form(request):
    if request.method == 'POST':
        form = ICTRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("ICT form submitted successfully.")
    return HttpResponse("Invalid request method.")


def ict_training_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        course = request.POST.get('course')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        ict_training_request = ICTTrainingRequest(
            name=name, course=course, email=email, phone=phone, location=location)
        ict_training_request.save()
        return redirect('success')
    return render(request, 'ict_training_request.html')


def ict_request(request):
    if request.method == 'POST':
        form = ICTRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ICTRequestForm()
    return render(request, 'home.html', {'form': form})

def submit_request(request):
    if request.method == 'POST':
        form = ICTRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Contact form submitted successfully.")
    return HttpResponse("Invalid request method.")





