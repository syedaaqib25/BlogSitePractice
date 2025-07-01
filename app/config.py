class Config:
    SECRET_KEY = 'your_secret_key_here'  # Replace with a secure key
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'  # Use PostgreSQL/MySQL in production
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = 'app/static/uploads'