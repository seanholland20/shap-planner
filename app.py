from flask import Flask
from .routes import main_routes
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    app.register_blueprint(main_routes)

    return app
