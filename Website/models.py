# We are going to use this to sort database models

# Now, importing from the current package "db" object
# Same as: from Website import db
from . import db 
# Custom class that we can inherit, that will give our user object some things, that are specific for our flask login
# Simply helps us login our users in
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # Start of relationship between "Note" and "User"...who created this Note ?
    # We must provide valid ID of an existing user to this field/column. (One-To-Many-Relationship)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # id is reference to class "User"

# Setup our "User" model. 
# We are going to store all our people, using this schema.
class User(db.Model, UserMixin):
    # Sometimes there might be users with same name.
    # We need some way to recognise them...that's where "primary_key" starts to play. (Integer)
    id = db.Column(db.Integer, primary_key=True)
    # Here we say, that email should be unique. No user can create profile with same email
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # Pretty much this will able every user to access there own notes
    # One more thing, "Note" used capital letter...when you do "Foreignkey" you use lowercase, and when you do relationships then capital letter
    notes = db.relationship('Note')

class ProductItem(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    # Nullable --> can have null value, but not neceserry
    describtion = db.Column(db.Text, unique=True, nullable=True)
    price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(200), unique=True)
    cartitem = db.relationship('CartItem', backref='Product')

class CartItem(db.Model):
    __tablename__='cartitem'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))



# When you want to store videos on the platform, or maybe you store reminders...
# Then we need to do the same thing, as this two classes
"""
class Files(db.Model):
    # Add all the fields, that we want to store
    # Lookup flask/sqlalchemy
    # Add foreign key to our user (Only when you have one to many relationship)
"""