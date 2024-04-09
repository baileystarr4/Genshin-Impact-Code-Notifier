from flask import Blueprint, render_template, request, flash
from Spreadsheet import *
from Notifier import *
from emailer import *

views = Blueprint('views', __name__)
notifier = Notifier()

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        first_name = request.form.get('firstName')
        provider = request.form.get('provider')
        password2 = request.form.get('password2')
        spreadsheet = Spreadsheet()

        if spreadsheet.find_user(phone_number) != -1:
            flash('Phone number already exists.', category='error')
        elif len(phone_number) < 9:
            flash('Phone number must be 9 digits.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif provider == "Other":
            flash('Carrier not currently supported.', category='error')
        else:
            spreadsheet.write_to_user_data_spreadsheet([phone_number,first_name, provider])
            flash('Success! You will receive text notifications when a new code is released.', category='success')
            notifier.send_welcome_text(phone_number, first_name, provider)
    return render_template("home.html")

@views.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        sure_check = request.form.get('sure_check')
        spreadsheet = Spreadsheet()
        user_row = spreadsheet.find_user(phone_number)
        if len(phone_number) < 9:
            flash('Phone number must be 9 digits.', category='error')
        elif not sure_check:
            flash('Please check the "are you sure box".', category='error')
        elif user_row == -1:
            flash('This phone number does not exist in our database. Please try again', category='error')
        else:
            spreadsheet.delete_user(user_row)
            flash('Success. You will no longer receive text notifications.', category='success')
    return render_template('unsubscribe.html')

@views.route('/contact_me', methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        body = request.form.get('body')
        

        if not name:
            flash('Please enter your name.', category='error')
        elif not email:
            flash('Please enter your email.', category='error')
        elif not subject:
            flash('Please enter a subject.', category='error')
        elif not body:
            flash('Please enter a message.', category='error')
        else:
            emailer = Emailer(name, email, subject, body)
            emailer.send_email()
            flash('Thank you for your feedback. I will respond via email as soon as possible.', category='success')
    return render_template("contact_me.html")