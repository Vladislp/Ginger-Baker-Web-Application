# This file is going to store all of the main views or the URL end points for the actual 
# functioning front end aspect of our website

# Store default roots for website

from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import stripe


# Setup blueprint for Flask application
views = Blueprint('views', __name__)


@views.route('/notes', methods=['GET', 'POST'])
# Now you can not get to the home page, unless you are login
@login_required
# This function will whenever we go to the slash route 
def notes():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    # We will be able to check, if we have authenticated
    return render_template("notes.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

#stripe.api_key = 'sk_test_51KibcBIEGhScLw0TaKrfJit7i1dKKZS6QzqTuhxX0DIDrAOFbIfUpVCL30TDHmjwGag9YgWrJY3420wmNs89Apa200GFBp1qp6'

#@views.route('/create-checkout-session', methods=['POST'])
#def create_checkout_session():
#  session = stripe.checkout.Session.create(
#    payment_method_types=['card'],
#    line_items=[{
#      'price_data': {
#        'currency': 'eur',
#        'product_data': {
#          'name': 'T-shirt',
#        },
#        
#      },
#      
#    }],
#    mode='payment',
#    success_url='http://127.0.0.1:5000/success',
#    cancel_url='http://127.0.0.1:5000/cancel',
#  )

#  return redirect(session.url, code=303)




# Decorator are an elegent way to extend functionality of our original function, without altering their source code.
# '/' --> route
@views.route('/', methods=['GET', 'POST'])
# Now you can not get to the home page, unless you are login
@login_required
# This function will whenever we go to the slash route 
def home():
    # We will be able to check, if we have authenticated
    return render_template("home.html", user=current_user)


@views.route('/menu', methods=['GET', 'POST'])
@login_required
def menu():
    return render_template("menu.html", user=current_user)

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html", user=current_user)

@views.route('/blog', methods=['GET', 'POST'])
def blog():
    return render_template("blog.html", user=current_user)

@views.route('/cart', methods=['GET', 'POST'])
def add_to_cart():
    return render_template("cart.html", user=current_user)

@views.route('/payment', methods=['GET', 'POST'])
def payment():
    return render_template("payment.html", user=current_user)

@views.route('/success', methods=['GET', 'POST'])
def success():
    return render_template("success.html", user=current_user)

@views.route('/cancel', methods=['GET', 'POST'])
def cancel():
    return render_template("cancel.html", user=current_user)




