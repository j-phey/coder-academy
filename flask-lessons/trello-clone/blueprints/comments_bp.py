from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.comment import CommentSchema, Comment
from auth import admin_required

comments_bp = Blueprint('comments', __name__)

# Create a route for when a user calls GET /comments
# Get all comments
# @comments_bp.route('/')
# @jwt_required() # If I want to secure this route with JWT - add this decorator
# def all_comments():
#     admin_required()
#     # select * from comments;
#     stmt = db.select(Comment)
#     comments = db.session.scalars(stmt).all()
#     return CommentSchema(many=True, exclude=['user.comments']).dump(comments) # dumps returns a string (text/html), dump serializes to the native language (Python) / JSON

# Get one comment
# @comments_bp.route('/<int:id>')
# @jwt_required() # Requires a login to get one comment
# def one_comment(id):
#     stmt = db.select(Comment).filter_by(id=id) # .where(Comment.id == id)
#     comment = db.session.scalar(stmt)
#     if comment: # Checks if valid comment id
#         return CommentSchema().dump(comment)
#     else:
#         return {'error': 'Comment not found'}, 404
    
# Create a new comment
# POST /comments
# POST /cards/<card_id>/comments
@comments_bp.route('/<int:card_id>/comments', methods=['POST']) 
@jwt_required()
def create_comment():
    # admin_required()
    comment_info = CommentSchema(only=['message']).load(request.json)
    comment = Comment(
        title = comment_info['title'],
        description = comment_info.get('description', ''), # If no description, just leave blank
        status = comment_info.get('status', 'To Do'), # If no status, default to 'To Do'
        user_id = get_jwt_identity()
    )
    
    db.session.add(comment)
    db.session.commit()
    return CommentSchema().dump(comment), 201

# Update a comment
@comments_bp.route('/<int:id>', methods=['PUT', 'PATCH'])
@jwt_required()
def update_comment(id):
    comment_info = CommentSchema(exclude=['id', 'date_created']).load(request.json)
    stmt = db.select(Comment).filter_by(id=id) # .where(Comment.id == id)
    comment = db.session.scalar(stmt)
    if comment: # Checks if valid comment id
        # Makes the following changes to these fields
        comment.title = comment_info.get('title', comment.title) 
        comment.description = comment_info.get('description', comment.description)
        comment.status = comment_info.get('status', comment.status)
        db.session.commit() # Re-commit it
        return CommentSchema().dump(comment)
    else:
        return {'error': 'Comment not found'}, 404
    
# Delete a comment
@comments_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_comment(id):
    admin_required()
    stmt = db.select(Comment).filter_by(id=id) # .where(Comment.id == id)
    comment = db.session.scalar(stmt)
    if comment: # Checks if valid comment id
        db.session.delete(comment)
        db.session.commit() # Commit the transaction (delete)
        return {}, 200
    else:
        return {'error': 'Comment not found'}, 404