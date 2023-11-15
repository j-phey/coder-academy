from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

# Always required to begin Flask app
app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://trello_dev:spameggs123@127.0.0.1:5432/trello'

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

@app.cli.command('db_create')
def db_create():
    db.drop_all() # This drops all tables to create the tables fresh
    db.create_all()
    print('Created tables')

@app.cli.command('db_seed') 
def db_seed():
    card = Card(
        title = 'Start the project',
        description = 'Stage 1 - Create ERD',
        date_created = date.today()
    )

    db.session.add(card) # This creates an entry - similar to git add .
    db.session.commit() # This commits the entry - similar to git commit -m

    print('Database seeded')

# Define an index/home page route
@app.route('/')
def index():
    return 'Hello world!'