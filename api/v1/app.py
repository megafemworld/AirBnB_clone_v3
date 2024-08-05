#!/usr/bin/python3
""" API MAIN handles connection """

from flask import Flask, Blueprint, make_response
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def tear_down_appcontext():
    """tear down app context"""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))

if __main__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')))
