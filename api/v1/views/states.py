#!/usr/bin/python3
"""view for state objects that handles all default RESTful API actions"""
from api.v1.views import app_views
from flask import Flask, jsonify, request
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def allstates():
    """retrieves list of all stte objects"""
    statelist = (storage.all(State).values())
    statedict = {}
    for eachstate in statelist:
        statedict.update(eachstate.to_dict())
    return jsonify(statedict)
