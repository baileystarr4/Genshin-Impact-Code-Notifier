from django import forms

PROVIDERS = {
    "default": "Choose an option...",
    "AT&T":"AT&T",
    "Boost Mobile": "Boost Mobile",
    "C-Spire":"C-Spire",
    "Cricket Wireless":"Cricket Wireless",
    "Consumer Cellular":"Consumer Cellular",
    "Google Project Fi":"Google Project Fi",
    "Metro PCS":"Metro PCS",
    "Mint Mobile":"Mint Mobile",
    "Page Plus":"Page Plus",
    "Republic Wireless":"Republic Wireless",
    "Sprint":"Sprint",
    "Straight Talk":"Straight Talk",
    "T-Mobile":"T-Mobile",
    "Ting":"Ting",
    "Tracfone":"Tracfone",
    "U.S. Cellular":"U.S. Cellular",
    "Verizon":"Verizon",
    "Virgin Mobile":"Virgin Mobile",
    "Xfinity Mobile":"Xfinity Mobile"
}

class SignUp(forms.Form):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(
        max_length=10, 
        widget=forms.TextInput(attrs={"class":"form-control"}))
    carrier = forms.ChoiceField(
        choices=PROVIDERS,
        widget=forms.Select(attrs={"class":"form-control"}))

class Unsubscribe(forms.Form):
    phone_number = forms.CharField(
        max_length=10, 
        widget=forms.TextInput(attrs={"class":"form-control"}))
    are_you_sure = forms.BooleanField()

class ContactMe(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.CharField(
        max_length=50, 
        widget=forms.EmailInput(attrs={"class":"form-control"}))
    subject = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control"}))
    body = forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control", "rows":"10"}))