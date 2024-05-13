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
            phone_number = form.cleaned_data['phone_number']
            first_name = form.cleaned_data['first_name']
            carrier = form.cleaned_data['carrier']

            try:
                # Is the phone number already in the database?
                User.objects.get(phone_number=phone_number)
                
            except:
                if carrier == "default":
                    messages.error(request, "Please choose a carrier.")
                else:
                    u = User(
                        phone_number=phone_number, 
                        first_name=first_name, 
                        carrier=carrier)
                    u.save()
                    
                    n = Notifier()
                    n.send_welcome_text(phone_number, first_name, carrier)
                    messages.success(
                        request, 
                        """Success! You will receive text notifications when a 
                           new code is released.""")

            else:    
                messages.error(
                    request, "This phone number is already a subscriber.")
                
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
            phone_number = form.cleaned_data['phone_number']

            try:
                # Is the phone number even in the database?
                User.objects.get(phone_number=phone_number).delete()
            except:
                messages.error(
                    request, "This phone number is not a subscriber.")
            else:
                messages.success(
                    request, 
                    "Success. You will no longer receive text notifications.")
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
                request,"Success. I will get back to you as soon as possible.")
    else:
        form = ContactMe()
    return render(request, "contact_me.html", {'form': form})