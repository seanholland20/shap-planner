import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///app.db')
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
