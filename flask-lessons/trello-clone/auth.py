from flask import abort
from flask_jwt_extended import get_jwt_identity
from models.user import User
from setup import db

def authorize(user_id=None): 
    # Check if user is an admin
    jwt_user_id = get_jwt_identity() # Checks identity of token
    stmt = db.select(User).filter_by(id=jwt_user_id)
    user = db.session.scalar(stmt) # Grab it with a scalar
    # If it's NOT the case that the user is an admin or user_id is truthy and matches the token
    # i.e. if user_id isn't passed in, they must be an admin
    if not (user.is_admin or (jwt_user_id == user_id)): 
        return abort(401)