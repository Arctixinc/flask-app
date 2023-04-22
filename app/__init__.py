from flask import Flask
from .routes import api
import os

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)
    return app
print(f"Listening on port {os.environ['PORT']}")
