from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import date
app = Flask(__name__) # Always required to begin Flask app
ma = Marshmallow(app)

# Set the database URI via SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'

# create the database object
db = SQLAlchemy(app)

# Create a SQL model - it's an entity in our database. 
# This is our Card entity
class Card(db.Model):
    __tablename__ = 'cards' # Sets the table name to 'cards' (instead of 'card')

    # Creating columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    date_created = db.Column(db.Date())

# create the Card Schema with Marshmallow, 
# it will provide the serialization needed for converting the data into JSON
class CardSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("id", "title", "description", "date", "status", "priority")

# single card schema, when one card needs to be retrieved
card_schema = CardSchema()

#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)

@app.cli.command('db_create')
def db_create():
    db.drop_all() # This drops all tables to create the tables fresh
    db.create_all()
    print('Created tables')

@app.cli.command('db_seed') 
def db_seed():
    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create ERD',
            date_created = date.today()
        ),

        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement Crud',
            date_created = date.today()
        ),

        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement JSONify of models',
            date_created = date.today()
        ) ,
    ]
    
    # You can add cards one by one
    # db.session.add(card1) # This creates an entry - similar to git add .
    # db.session.add(card2)
    # db.session.add(card3)

    db.session.add_all(cards)
    db.session.commit() # This commits the entry - similar to git commit -m

    print('Database seeded')

# Define an index/home page route
@app.route('/')
def index():
    return 'Hello world!'

@app.route("/cards", methods=["GET"])
def get_cards():
    #get all the cards from the database table
    stmt = db.select(Card)
    cards = db.session.scalars(stmt)
    # Convert the cards from the database into a JSON format and store them in result
    result = cards_schema.dump(cards)
    #return result in JSON format
    return jsonify(result)