from flask import Blueprint
from setup import db, bcrypt
from models.card import Card
from models.user import User
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create') # Creates the tables above
def db_create():
    db.drop_all() # This drops all tables to create the tables fresh
    db.create_all() 
    print('Created tables')

@db_commands.cli.command('seed') # Creates entries in the tables
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