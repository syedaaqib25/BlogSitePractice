from flask import Blueprint, flash, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Post
from app import db
from app.forms import PostForm  # Import the form

posts_bp = Blueprint('posts', __name__)

@posts_bp.route('/')
def index():
    posts = Post.query.filter_by(draft=False).all()
    return render_template('index.html', posts=posts)

@posts_bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    form = PostForm()  # Create the form instance
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        draft = form.draft.data
        post = Post(title=title, content=content, draft=draft, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts.index'))
    return render_template('create_post.html', form=form)  # Pass the form to the template

@posts_bp.route('/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if post.author != current_user:
        flash('You do not have permission to edit this post.')
        return redirect(url_for('posts.index'))
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.draft = 'draft' in request.form
        db.session.commit()
        return redirect(url_for('posts.index'))
    return render_template('edit_post.html', post=post)