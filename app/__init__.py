# __init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .routes import blueprint as main
    app.register_blueprint(main)

    return app
