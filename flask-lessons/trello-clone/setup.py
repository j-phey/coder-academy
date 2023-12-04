from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from os import environ
from marshmallow.exceptions import ValidationError

app = Flask(__name__) # Always required to begin Flask app

# Set the database URI via SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URI')

app.config['JWT_SECRET_KEY'] = environ.get('JWT_KEY')

db = SQLAlchemy(app) # Create the database object
ma = Marshmallow(app) # Create an instance of Marshmallow and connect with our 'app'
bcrypt = Bcrypt(app) # Create an instance of Bcrypt for our app
jwt = JWTManager(app) # Create an instance of JWTManager

@app.errorhandler(401)
def unauthorized(err):
    return {'error': 'You are not authorised!'}

# Validation for missing information on registering user, etc. / not a valid email address
@app.errorhandler(ValidationError)
def validation_error(err):
    return {'error': err.messages}