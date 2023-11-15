from flask import Blueprint, render_template, request, flash
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@views.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        first_name = request.form.get('firstName')
        carrier = request.form.get('carrier')
        password2 = request.form.get('password2')

        # user = User.query.filter_by(phone_number=phone_number).first()
        if user:
            flash('Phone number already exists.', category='error')
        elif len(phone_number) < 9:
            flash('Phone number must be 9 digits.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif carrier == "Other":
            flash('Carrier not currently supported.', category='error')
        else:
            # new_user = User(phone_number=phone_number, first_name=first_name, carrier=carrier)
            # db.session.add(new_user)
            # db.session.commit()
            flash('Success! You will receive your first notifiction shortly.', category='success')

    return render_template("sign_up.html")

@views.route('/unsubscribe', methods=['GET', 'POST'])
def unsubscribe():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        sure_check = request.form.get('sure_check')
        # user = User.query.filter_by(phone_number=phone_number).first()
        if len(phone_number) < 9:
            flash('Phone number must be 9 digits.', category='error')
        elif not sure_check:
            flash('Please check the "are you sure box".', category='error')
        # elif not user:
        #     flash('This phone number does not exist in our database. Please try again', category='error')
        # else:
        #     db.session.delete(user)
        #     db.session.commit()
            flash('Success. You will no longer receive text notifications.', category='success')

    return render_template('unsubscribe.html')

@views.route('/about_me', methods=['GET'])
def about_me():
    return render_template("about_me.html")