# cli_bp.py sorts out all our database stuff - creating tables, seeding tables, creating rows, seeding rows etc.

from flask import Blueprint
from setup import db, bcrypt
from models.card import Card
from models.user import User
from models.comment import Comment
from datetime import date

db_commands = Blueprint('db', __name__)

@db_commands.cli.command('create') # Creates the tables above
def db_create():
    db.drop_all() # This drops all tables to create the tables fresh
    db.create_all() 
    print('Created tables')

@db_commands.cli.command('seed') # Creates entries in the tables
def db_seed():

    # CREATE USERS
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
    db.session.add_all(users) # All the users first, before the cards
    db.session.commit() # This commits the entry - similar to git commit -m. Gotta commit users so cards can access the user_id

    # CREATE CARDS
    cards = [
        Card(
            title = 'Start the project',
            description = 'Stage 1 - Create ERD',
            status='Done',
            date_created = date.today(),
            user_id = users[0].id # aka user_id 1
        ),

        Card(
            title = 'ORM Queries',
            description = 'Stage 2 - Implement Crud',
            status='In Progress',
            date_created = date.today(),
            user_id = users[1].id # aka user_id 2
        ),

        Card(
            title = 'Marshmallow',
            description = 'Stage 3 - Implement JSONify of models',
            status='In Progress',
            date_created = date.today(),
            user_id = users[0].id # aka user_id 1
        ),
    ]
    
    # You can add cards one by one
    # db.session.add(card1) # This creates an entry - similar to git add .
    # db.session.add(card2)
    # db.session.add(card3)

    db.session.add_all(cards) # Add the cards
    db.session.commit() # This commits the entry - similar to git commit -m

    comments = [
        Comment(
            message = "Comment 1",
            user_id=users[0].id,
            card_id=cards[1].id # References the created cards above
        ),
        Comment(
            message = "Comment 2",
            user_id=users[1].id,
            card_id=cards[1].id # References the created cards above
        ),
        Comment(
            message = "Comment 3",
            user_id=users[1].id,
            card_id=cards[0].id # References the created cards above
        )
    ]

    db.session.add_all(comments) # Add the cards
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