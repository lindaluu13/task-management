from flask import Blueprint, request, jsonify
from .models import db, User
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity


auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if 'name' not in data or not data['name']:
        return jsonify(message="Name is required."), 400
    if not data.get('email') or not data.get('password'):
        return jsonify(message="Email and password are required."), 400

    user = User(name=data['name'], email=data['email'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    token = create_access_token(identity=user.id)

    return jsonify(message="User created successfully.", user={'id': user.id, 'name': user.name, 'email': user.email}, token=token), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and user.check_password(data['password']):
        token = create_access_token(identity=str(user.id))
        return jsonify(message="Login successful.", access_token=token)
    return jsonify(message="Invalid email or password."), 401


@auth_bp.route('/login', methods=['PUT'])
@jwt_required() 
def update_user_info():
    # Get user id through JWT
    user_id = get_jwt_identity()
    user = User.query.get(user_id)
    
    if not user:
        return jsonify(message="User not found."), 404
    
    data = request.get_json()

    # Update user infos
    if 'name' in data:
        user.name = data['name']
    
    if 'email' in data:
        # Verify if email in use
        if User.query.filter_by(email=data['email']).first():
            return jsonify(message="Email already in use."), 400
        user.email = data['email']
    
    if 'current_password' in data and 'new_password' in data:
        # Verify current password
        if user.check_password(data['current_password']):
            user.set_password(data['new_password'])
        else:
            return jsonify(message="Incorrect current password."), 401

    db.session.commit()

    return jsonify(message="User information updated successfully.", user={"id": user.id, "name": user.name, "email": user.email})

