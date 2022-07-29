#!/usr/bin/python3
"""define routes for the app_views blueprint"""
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
@app_views.route('/stats', strict_slashes=False)
def stats():
    """retrieves the number of each object by type"""
    objcounts = {'amenities': 'Amenity', 'cities': 'City', 'places': 'Place',
                 'reviews': 'Review', 'states': 'State', 'users': 'User'}
    for key, value in objcounts.items():
        objcounts[key] = storage.count(value)
    return jsonify(objcounts)
