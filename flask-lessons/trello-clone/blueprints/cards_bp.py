from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.card import CardSchema, Card
from auth import authorize
from blueprints.comments_bp import comments_bp

cards_bp = Blueprint('cards', __name__, url_prefix='/cards')

# Create a route for when a user calls GET /cards
# Get all cards
@cards_bp.route('/')
@jwt_required() # If I want to secure this route with JWT - add this decorator
def all_cards():
    authorize()
    # select * from cards;
    stmt = db.select(Card)
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True, exclude=['user.cards']).dump(cards) # dumps returns a string (text/html), dump serializes to the native language (Python) / JSON

# Get one card
@cards_bp.route('/<int:id>')
@jwt_required() # Requires a login to get one card
def one_card(id):
    stmt = db.select(Card).filter_by(id=id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card: # Checks if valid card id
        return CardSchema().dump(card)
    else:
        return {'error': 'Card not found'}, 404
    
# Create a new card
@cards_bp.route('/', methods=['POST']) # Can be '/' because we are just POSTing or creating a new card
@jwt_required()
def create_card():
    # admin_required()
    card_info = CardSchema(exclude=['id', 'date_created']).load(request.json)
    card = Card(
        title = card_info['title'],
        description = card_info.get('description', ''), # If no description, just leave blank
        status = card_info.get('status', 'To Do'), # If no status, default to 'To Do'
        user_id = get_jwt_identity()
    )

    db.session.add(card)
    db.session.commit()
    return CardSchema().dump(card), 201

# Update a card
@cards_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_card(id):
    card_info = CardSchema(exclude=['id', 'date_created']).load(request.json)
    stmt = db.select(Card).filter_by(id=id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card: # Checks if valid card id
        # Check if actual owner of the card
        authorize(card.user_id) # Compares user_id and the jwt_user_id token in auth.py
        # Makes the following changes to these fields
        card.title = card_info.get('title', card.title) 
        card.description = card_info.get('description', card.description)
        card.status = card_info.get('status', card.status)
        db.session.commit() # Re-commit it
        return CardSchema().dump(card)
    else:
        return {'error': 'Card not found'}, 404
    
# Delete a card
@cards_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_card(id):
    stmt = db.select(Card).filter_by(id=id) # .where(Card.id == id)
    card = db.session.scalar(stmt)
    if card: # Checks if valid card id
        # Check if actual owner of the card
        authorize(card.user_id) # Compares user_id and the jwt_user_id token in auth.py
        db.session.delete(card)
        db.session.commit() # Commit the transaction (delete)
        return {}, 200
    else:
        return {'error': 'Card not found'}, 404
    
cards_bp.register_blueprint(comments_bp)
# Registering a BP basically adds the contents of it (routes/commands) to another BP or the app.
#  Without that, the app/parent bp wouldn't know about it. The connection is not made automatically
#  because we might want to test the routes in isolation, and Flask has no way to know in advance if
#  we want to attach them as a child to another bp or to the app directly.