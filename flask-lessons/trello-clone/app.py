from flask import abort, jsonify
from models.card import CardSchema
from setup import app
from blueprints.cli_bp import db_commands
from blueprints.users_bp import users_bp
from blueprints.cards_bp import cards_bp # Notation: from folder.file import instance

# Call the cli_bp blueprint
app.register_blueprint(db_commands)

# Call the users_bp blueprint
app.register_blueprint(users_bp)

# Call the cards_bp blueprint
app.register_blueprint(cards_bp)
