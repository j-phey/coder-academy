from flask import request, abort, jsonify
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User, UserSchema
from models.card import Card, CardSchema
from setup import app, db, ma, bcrypt, jwt
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp

def admin_required():
    # Check if user is an admin
    user_email = get_jwt_identity() # Checks the identity from the token
    stmt = db.select(User).where(User.email == user_email)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        return abort(401)

# single card schema, when one card needs to be retrieved
card_schema = CardSchema()

#multiple card schema, when many cards need to be retrieved
cards_schema = CardSchema(many=True)

# Call the cli_bp blueprint
app.register_blueprint(db_commands)

# Call the users_bp blueprint
app.register_blueprint(users_bp)

# Define an index/home page route
@app.route('/')
def index():
    return 'Hello world!'

# Create a route for when a user calls GET /cards
@app.route('/cards')
@jwt_required() # If I want to secure this route with JWT - add this decorator
def all_cards():
    # admin_required()

    # select * from cards;
    stmt = db.select(Card).order_by(Card.title.desc()) # Pass the class itself as a paramater that you want to SELECT on. 
    cards = db.session.scalars(stmt).all()
    return CardSchema(many=True).dump(cards) # dumps returns a string (text/html), dump serializes to the native language (Python) / JSON

@app.errorhandler(IntegrityError)
def integrity_error(err):
    return {'error': 'Generic IntegrityError!'}, 409

@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You are not authorised!'}

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