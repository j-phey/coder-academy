from setup import db, ma
from datetime import datetime
from marshmallow import fields

# Create a SQL model - it's an entity in our database. 
# This is our Card entity / TABLE
class Card(db.Model):
    __tablename__ = 'cards' # Sets the table name to 'cards' (instead of 'card')

    # Creating columns
    id = db.Column(db.Integer, primary_key=True) # This is the primary key

    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text()) # You technically don't need parenthesis if not specifying a limit
    status = db.Column(db.String(30), default='To Do') 
    date_created = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d')) 

    # Creating a foreign key - establishes relationship at the database level with User table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False) # 'users.id' is table_name.field (from user.py model)
    # SQLAlchemy relationship - nests an instance of a related model in this one
    user = db.relationship('User', back_populates='cards') # Pass the model class name for the relationship. back_populates links the relationship with user model, where ='' is same as db.relationship variable in other table
    comments = db.relationship('Comment', back_populates='card') # Back populate is not a table name. It's the name of the field in the other model that this line relates to.

# create the Card Schema with Marshmallow, 
# it will provide the serialization needed for converting the data into JSON
# aka is serializes the data - converts it into JSON
class CardSchema(ma.Schema):
    # Tell marshmallow to nest a UserSchema instance when serialising
    user = fields.Nested('UserSchema', exclude=['password']) # When you nest the user, exclude the password
    
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "status", "date_created", "user") # "user" passes the user details here from the nested field above

# single card schema, when one card needs to be retrieved
card_schema = CardSchema()

#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)