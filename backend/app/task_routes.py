from flask import Blueprint, request, jsonify
from .models import db, Task
from flask_jwt_extended import jwt_required, get_jwt_identity

tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tasks', methods=['GET', 'POST'])
@jwt_required()
def manage_tasks():
    user_id = get_jwt_identity()
    if request.method == 'POST':
        data = request.get_json()
        task = Task(title=data['title'], deadline=data.get('deadline'), description=data.get('description'), user_id=user_id)
        
        db.session.add(task)
        db.session.commit()
        # converts task in object JSON
        return jsonify(task.to_dict()), 201

    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([task.to_dict() for task in tasks]), 200

@tasks_bp.route('/tasks/<int:id>', methods=['PUT', 'DELETE'])
@jwt_required()
def task_detail(id):
    task = Task.query.get_or_404(id)
    if request.method == 'PUT':
        data = request.get_json()
        task.title = data.get('title', task.title)
        task.status = data.get('status', task.status)
        task.description = data.get('description', task.description)
        task.deadline = data.get('deadline', task.deadline)
        db.session.commit()
        return jsonify(task.to_dict()), 200
    else:
        db.session.delete(task)
        db.session.commit()
        return '', 204 # No content
