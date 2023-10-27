from flask import Blueprint, render_template, request, flash, jsonify
from .models import User
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        phone_number = request.form.get('phone_number')
        first_name = request.form.get('firstName')
        carrier = request.form.get('carrier')
        password2 = request.form.get('password2')

        user = User.query.filter_by(phone_number=phone_number).first()
        if user:
            flash('Phone number already exists.', category='error')
        elif len(phone_number) < 9:
            flash('Phone number must be 9 digits.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif carrier == "Other":
            flash('Carrier not currently supported.', category='error')
        else:
            new_user = User(phone_number=phone_number, first_name=first_name, carrier=carrier)
            db.session.add(new_user)
            db.session.commit()
            flash('Success! You will receive your first notifiction shortly.', category='success')

    return render_template("home.html")


@views.route('/unsubscribe', methods=['POST'])
def unsubscribe():  
    user = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    userId = user['id']
    user = User.query.get(userId)
    if user:
        db.session.delete(user)
        db.session.commit()

    return jsonify({})