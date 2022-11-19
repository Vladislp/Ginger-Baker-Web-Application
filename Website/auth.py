from flask import Blueprint, render_template, request, flash, redirect, url_for
# import from "models.py" user model
from .models import User
# Some import, that will allow to hash password
# Password hashing is used to verify the integrity of your password, sent during login, against the stored hash so that your...
# actual password never has to be stored in "plain text"
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

from flask_login import login_user, login_required, logout_user, current_user

# Setup blueprint for Flask application
auth = Blueprint('auth', __name__)

# Setup routes and URL
# So that we can in URL type something.something.something/Login
# End we will go to the desired web page

# method=['GET', 'POST'] we can accept now 'GET/POST'
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # We want to somehow confirm user, that he is inded created account
        email = request.form.get('email')
        password = request.form.get('password')
        # We need to query database, to find entres
        # Filter all the users, that has this email
        user = User.query.filter_by(email=email).first()
        if user:
            # Hash password and check hash in database
            if check_password_hash(user.password, password):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again', category='error')
        else:
            flash('Email does not exist.', category='error')

    # text="Testing" it means that inside of my login.HTML template i can access the variable text
    # return render_template("login.html", text="Testing", user="Tim")
    return render_template("login.html", user=current_user)

@auth.route('/logout')
# We can't access this root, if user is not logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# We need POST request to store data, that comes from page (enclosed in the body of the request message)
# We need GET request to access webpage, simply if we enter URL in to the search bar...then it is a GET request
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        # Here we .get information from "Sign-up" page.
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        # Now we need to check, if our information is valid
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Passwords must be at least 7 characters ', category='error')
        else:
            # 'sha256' = hashing algorith
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            # Add "new_user" to DB
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            # Return a "redirect" url for "Homepage"
            # We can do this: "url_for('views.home')" because it is in our blueprint
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)