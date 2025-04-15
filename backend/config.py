## Konfigurasi database

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#ADMIN  
class Config:
    SECRET_KEY = "very_secret_key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMIN_ROLE = "admin"
    USER_ROLE = "user"

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)  # Enable CORS for all routes
    return app  