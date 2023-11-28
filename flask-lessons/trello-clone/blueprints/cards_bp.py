from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from setup import db
from models.card import CardSchema, Card
from auth import admin_required

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

# Create a route for when a user calls GET /cards
@cards_bp.route('/')
@jwt_required() # If I want to secure this route with JWT - add this decorator
def all_cards():
    # admin_required()

    # select * from cards;
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards) # dumps returns a string (text/html), dump serializes to the native language (Python) / JSON

# Get one card
@cards_bp.route('/<int:id>')
@jwt_required() # Requires a login to get one card
def one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    if card: # Checks if valid card id
        return CardSchema().dump(card)
    else:
        return {'error': 'Card not found'}, 404
    
# Create a new card
@cards_bp.route('/', methods=['POST']) # Can be '/' because we are just POSTing or creating a new card
def create_card():
    card_info = CardSchema(exclude=['id', 'date_created']).load(request.json)
    print(card_info)
    return {}