from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import User, Post
from app import db

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if current_user.role != 'admin':
        flash('Access denied.')
        return redirect(url_for('posts.index'))
    users = User.query.all()
    posts = Post.query.all()
    return render_template('admin_dashboard.html', users=users, posts=posts)