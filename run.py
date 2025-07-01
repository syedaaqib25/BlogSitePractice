from app import create_app, db

app = create_app()

# Auto-create tables on startup (for SQLite or initial deployment)
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run()
