from setup import db, ma
from marshmallow import fields

class User(db.Model): # SPECIFYING A USERS TABLE
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True) # Cannot be null, i.e. it's required. Every user must be unique with email address.
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False) # Should they have admin rights

    # Establish relationship with card.py model
    cards = db.relationship('Card') # Get cards owned by queried user

# Use Marshmallow
class UserSchema(ma.Schema):
    cards = fields.Nested('CardSchema', exclude=['user'])

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'cards')