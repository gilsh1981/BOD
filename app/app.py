# app.py
from flask import Flask
from config import Config
from app.routes import blueprint as routes_blueprint

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)

# Register the routes blueprint
app.register_blueprint(routes_blueprint, url_prefix='')
