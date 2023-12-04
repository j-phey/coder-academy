from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from setup import db
from models.comment import CommentSchema, Comment
from auth import authorize

comments_bp = Blueprint('comments', __name__, url_prefix='/<int:card_id>/comments')

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
@comments_bp.route('/', methods=['POST'])
@jwt_required()
def create_comment(card_id):
    # admin_required()
    comment_info = CommentSchema(only=['message']).load(request.json)
    comment = Comment(
        message = comment_info['message'],
        user_id = get_jwt_identity(),
        card_id = card_id
    )
    
    db.session.add(comment)
    db.session.commit()
    return CommentSchema().dump(comment), 201

# Update a comment
# PUT /cards/<card_id>/comments/<comment_id>
@comments_bp.route('/<int:comment_id>', methods=['PUT', 'PATCH']) # Because this route attaches to the comments blueprint, it implies its a comment id <int:id>
@jwt_required()
def update_comment(card_id, comment_id):
    comment_info = CommentSchema(only=['message']).load(request.json) # We can only update the comment message, so use only=['message']
    stmt = db.select(Comment).filter_by(id=comment_id) # .where(Comment.id == id)
    comment = db.session.scalar(stmt)
    if comment: # Checks if valid comment id
        authorize(comment.user_id) # Admin or person who made comment
        # Makes the following changes to these fields
        comment.message = comment_info.get('message', comment.message) 
        db.session.commit() # Re-commit it
        return CommentSchema().dump(comment)
    else:
        return {'error': 'Comment not found'}, 404
    
# Delete a comment
# DELETE /cards/<card_id>/comments/<comment_id>
@comments_bp.route('/<int:comment_id>', methods=['DELETE'])
@jwt_required()
def delete_comment(card_id, comment_id):
    # admin_required()
    stmt = db.select(Comment).filter_by(id=comment_id) # .where(Comment.id == id)
    comment = db.session.scalar(stmt)
    if comment: # Checks if valid comment id
        authorize(comment.user_id) # Admin or person who made comment
        db.session.delete(comment)
        db.session.commit() # Commit the transaction (delete)
        return {}, 200
    else:
        return {'error': 'Comment not found'}, 404