from flask import app, render_template
from forms import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process the form data (e.g., authenticate user)
        return 'Login successful!'
    return render_template('login.html', form=form)