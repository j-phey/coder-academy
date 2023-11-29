from setup import db, ma
from datetime import datetime
from marshmallow import fields

# Create a SQL model - it's an entity in our database. 
# This is our Card entity / TABLE
class Comment(db.Model):
    __tablename__ = 'comments' # Sets the table name to 'cards' (instead of 'card')

    # Creating columns
    id = db.Column(db.Integer, primary_key=True) # This is the primary key

    message = db.Column(db.Text()) # You technically don't need parenthesis if not specifying a limit

    # Creating a foreign key - establishes relationship at the database level with User table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # 'users.id' is table_name.field (from user.py model)
    user = db.relationship('User', back_populates='comments')
    
    # SQLAlchemy relationship - nests an instance of a related model in this one
    card_id = db.Column(db.Integer, db.ForeignKey('cards.id'), nullable=False)
    card = db.relationship('Card', back_populates='comments') # Pass the model class name for the relationship. back_populates links the relationship with comments model, where ='' is same as db.relationship variable in other table

# create the Card Schema with Marshmallow, 
# it will provide the serialization needed for converting the data into JSON
# aka is serializes the data - converts it into JSON
class CommentSchema(ma.Schema):
    # Tell marshmallow to nest a UserSchema instance when serialising
    user = fields.Nested('UserSchema', only=['id', 'name']) # When you nest the user, only include these fields
    card = fields.Nested('CardSchema', only=['id', 'title']) # When you nest the card, only include these fields

    class Meta:
        # Fields to expose
        fields = ("id", "message", "user", "card") # "user" passes the user details here from the nested field above. Same with "card"
