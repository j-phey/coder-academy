from flask import abort
from flask_jwt_extended import  get_jwt_identity
from models.user import User
from setup import db

def admin_required():
    # Check if user is an admin
    user_email = get_jwt_identity() # Checks the identity from the token
    stmt = db.select(User).where(User.email == user_email)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        return abort(401)