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
    cards = db.relationship('Card', back_populates='user') # Get cards owned by queried user. back_populates links the relationship with card model, where ='' is same as db.relationship variable in other table
    comments = db.relationship('Comment', back_populates='user') # 'Comment' relationship to Comment model, back populate to this model, user

# Use Marshmallow
class UserSchema(ma.Schema):
    cards = fields.Nested('CardSchema', exclude=['user'], many=True) # Need many=True because cards is a list

    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin', 'cards')