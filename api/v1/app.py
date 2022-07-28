#!/usr/bin/python3
"""start flask, register a blueprint and define status of API route"""

from flask import Flask
from models import storage
from api.v1.views import app_views
import os

# create variable app, instance of Flask
app = Flask(__name__)
# register the blueprint app_views to Flask instance app
app.register_blueprint(app_views)


# register function to be called when the app context ends
@app.teardown_appcontext
def teardown_storage(self):
    """call functions to be executed when app context ends"""
    storage.close()

if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
