#!/usr/bin/python3
"""define /status route  on the object app_views"""
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', strict_slashes=False)
def status():
    """defines route which returns the status of the api"""
    api_status = {"status": "OK"}
    return jsonify(api_status)
