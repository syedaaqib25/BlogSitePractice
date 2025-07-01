from app import create_app, db
from flask_migrate import upgrade

app = create_app()

@app.before_first_request
def do_upgrade():
    upgrade()
