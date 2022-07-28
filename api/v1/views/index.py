#!/usr/bin/python3
"""define /status route  on the object app_views"""
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage

# an endpoint that retieves status of the API
@app_views.route('/status', strict_slashes=False)
def status():
    """defines route which returns the status of the api"""
    api_status = {"status": "OK"}
    return jsonify(api_status)

# creating an endpoin that retrieves the number of each obj by type
@app_views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """retrieves the number of each object by type"""
    for each object in storage:
        run the count method on it
        print the count...or added to the dictionary to be jsonified
