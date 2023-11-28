from flask import Blueprint
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