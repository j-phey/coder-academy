from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import json
from flask_bcrypt import Bcrypt

app = Flask(__name__) # Always required to begin Flask app

# Set the database URI via SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'

# create the database object
db = SQLAlchemy(app)

ma = Marshmallow(app) # Create an instance of Marshmallow and connect with our 'app'
bcrypt = Bcrypt(app) # Create an instance of Bcrypt for our app

# Create a SQL model - it's an entity in our database. 
# This is our Card entity / TABLE
class Card(db.Model):
    __tablename__ = 'cards' # Sets the table name to 'cards' (instead of 'card')

    # Creating columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    status = db.Column(db.Text) # You technically don't need parenthesis if not specifying a limit
    date_created = db.Column(db.Date) 

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

class User(db.Model): # SPECIFYING A USERS TABLE
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True) # Cannot be null, i.e. it's required. Every user must be unique with email address.
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False) # Should they have admin rights

@app.cli.command('db_create') # Creates the tables above
def db_create():
    db.drop_all() # This drops all tables to create the tables fresh
    db.create_all() 
    print('Created tables')

@app.cli.command('db_seed') # Creates entries in the tables
def db_seed():

    users = [ 
    User(
        email='admin@spam.com',
        password=bcrypt.generate_password_hash('spinynorman').decode('utf8'), # Encrypts the pw using bcrypt, formats as utf8 
        is_admin=True
    ),

    User(
        name='John Cleese',
        email='cleese@spam.com',
        password=bcrypt.generate_password_hash('tisbutascratch').decode('utf8') # Encrypts the pw using bcrypt, formats as utf8
    )
]

    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create ERD',
            status='Done',
            date_created = date.today()
        ),

        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement Crud',
            status='In Progress',
            date_created = date.today()
        ),

        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement JSONify of models',
            status='In Progress',
            date_created = date.today()
        ) ,
    ]
    
    # You can add cards one by one
    # db.session.add(card1) # This creates an entry - similar to git add .
    # db.session.add(card2)
    # db.session.add(card3)

    db.session.add_all(users)
    db.session.add_all(cards)
    db.session.commit() # This commits the entry - similar to git commit -m

    print('Database seeded')


# CLI COMMANDS

# @app.cli.command('all_cards')
# def all_cards():
#     # select * from cards;
#     stmt = db.select(Card).order_by(Card.title.desc()) # Pass the class itself as a paramater that you want to SELECT on. 
#     print(stmt)
#     # This produces:  SELECT cards.id, cards.title, cards.description, cards.date_created 
#                     # FROM cards
    
#     # cards = db.session.execute(stmt)
#     # print(cards.all()) # Produces: [(<Card 1>,), (<Card 2>,), (<Card 3>,)]
    
#     cards = db.session.scalars(stmt).all()
#     # print(cards.all()) # Produces [<Card 1>, <Card 2>, <Card 3>]

#     for card in cards:
#         print(card.__dict__) 


@app.route('/cards')
def all_cards():
    # select * from cards;
    stmt = db.select(Card).order_by(Card.title.desc()) # Pass the class itself as a paramater that you want to SELECT on. 
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards) # dumps returns a string (text/html), dump serializes to the native language (Python) / JSON


# Define an index/home page route
@app.route('/')
def index():
    return 'Hello world!'

# # Create a route for when a user calls GET /cards
# @app.route("/cardss", methods=["GET"])
# def get_cards():
#     #get all the cards from the database table
#     stmt = db.select(Card)
#     cards = db.session.scalars(stmt)
#     # return CardSchema(many=True).dump(cards)

#     # Convert the cards from the database into a JSON format and store them in result
#     result = cards_schema.dump(cards)
#     #return result in JSON format
#     return jsonify(result)