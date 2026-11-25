from django import forms

class SignUp(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}))
    signup_email = forms.CharField(
        max_length=50, 
        widget=forms.EmailInput(attrs={"class":"form-control"}))

class Unsubscribe(forms.Form):
    unsubscribe_email = forms.CharField(
        max_length=50, 
        widget=forms.EmailInput(attrs={"class":"form-control"}))
    are_you_sure = forms.BooleanField()

class ContactMe(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}))
    contactme_email = forms.CharField(
        max_length=50, 
        widget=forms.EmailInput(attrs={"class":"form-control"}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}))
    body = forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control", "rows":"10"}))