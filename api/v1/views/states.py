#!/usr/bin/python3
"""view for state objects that handles all default RESTful API actions"""
from api.v1.views import app_views
from flask import Flask, jsonify, request, abort
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def allstates():
    """retrieves list of all stte objects"""
    statedict = (storage.all(State).values())
    statelist = []
    for eachstate in statedict:
        statelist.append(eachstate.to_dict())
    return jsonify(statelist)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def selectstate(state_id):
    """retrieves a state obj based on provided state id"""
    # get dictionary of all states
    stateobjs = storage.all(State).values()
    if len(stateobjs) != 0:
        for stateobj in stateobjs:
            if stateobj.id == state_id:
                return jsonify(stateobj.todict())
        abort(404)
