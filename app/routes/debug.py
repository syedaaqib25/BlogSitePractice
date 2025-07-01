from flask import Blueprint, jsonify
from app.models import User  # or your Post model
from app import db

debug_bp = Blueprint('debug', __name__)

@debug_bp.route('/debug/users')
def show_users():
    users = User.query.all()
    return jsonify([u.username for u in users])
