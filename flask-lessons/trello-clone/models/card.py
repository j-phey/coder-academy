from setup import db, ma
from datetime import datetime

# Create a SQL model - it's an entity in our database. 
# This is our Card entity / TABLE
class Card(db.Model):
    __tablename__ = 'cards' # Sets the table name to 'cards' (instead of 'card')

    # Creating columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text())
    status = db.Column(db.String(30), default='To Do') # You technically don't need parenthesis if not specifying a limit
    date_created = db.Column(db.Date, default=datetime.now().strftime('%Y-%m-%d')) 

# create the Card Schema with Marshmallow, 
# it will provide the serialization needed for converting the data into JSON
# aka is serializes the data - converts it into JSON
class CardSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "status", "date_created")

# single card schema, when one card needs to be retrieved
card_schema = CardSchema()

#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)