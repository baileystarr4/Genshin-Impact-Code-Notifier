from django.shortcuts import render
from django.contrib import messages
from scripts.emailer import *
from scripts.notifier import *
from .models import User
from .forms import SignUp, Unsubscribe, ContactMe

def home(request):
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            email = form.cleaned_data['signup_email']
            first_name = form.cleaned_data['first_name']
            try:
                # Is the phone number already in the database?
                User.objects.get(email=email)
                
            except:
                u = User(
                    email=email, 
                    first_name=first_name)
                u.save()
                
                n = Notifier()
                n.send_welcome_text(email, first_name)
                messages.success(
                    request, 
                    """Success! You will receive email notifications when a 
                        new code is released.""")

            else:    
                messages.error(
                    request, "This email is already a subscriber.")
                
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = SignUp()
    return render(request, "home.html", {'form': form})

def unsubscribe(request):
    if request.method == 'POST':
        form = Unsubscribe(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            try:
                # Is the phone number even in the database?
                User.objects.get(email=email).delete()
            except:
                messages.error(
                    request, "This email is not a subscriber.")
            else:
                messages.success(
                    request, 
                    "Success. You will no longer receive email notifications.")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    else:
        form = Unsubscribe()
    return render(request,'unsubscribe.html', {'form': form})

def contact_me(request):
    if request.method == 'POST':
        form = ContactMe(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
        
            emailer = Emailer(name, email, subject, body)
            emailer.send_email()
            messages.success(
                request,"Success! I will get back to you as soon as possible.")
    else:
        form = ContactMe()
    return render(request, "contact_me.html", {'form': form})