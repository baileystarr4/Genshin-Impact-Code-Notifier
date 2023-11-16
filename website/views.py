from flask import Blueprint, render_template, request, flash
from Spreadsheet import *

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@views.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
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
            flash('Success! You will receive a text notification when a new code is released.', category='success')

    return render_template("sign_up.html")

@views.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        sure_check = request.form.get('sure_check')
        spreadsheet = Spreadsheet()
        if len(phone_number) < 9:
            flash('Phone number must be 9 digits.', category='error')
        elif not sure_check:
            flash('Please check the "are you sure box".', category='error')
        elif spreadsheet.find_user(phone_number) == -1:
            flash('This phone number does not exist in our database. Please try again', category='error')
        else:
            spreadsheet.delete_user(phone_number)
            flash('Success. You will no longer receive text notifications.', category='success')

    return render_template('unsubscribe.html')

@views.route('/about_me', methods=['GET'])
def about_me():
    return render_template("about_me.html")