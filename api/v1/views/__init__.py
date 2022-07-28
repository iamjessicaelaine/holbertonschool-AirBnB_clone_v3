#!/usr/bin/python3
"""treat my views directory as a module & execute this code when is loaded"""

from flask import Blueprint
from api.v1.view.index import *

# create a Blueprint for app_views
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
