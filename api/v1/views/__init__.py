#!/usr/bin/python3
"""
File to make views a package for Flask API
"""
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.index import *  # nopep8
from api.v1.views.states import *  # nopep8
from api.v1.views.cities import *  # nopep8
from api.v1.views.amenities import *  # nopep8
from api.v1.views.users import *  # nopep8
from api.v1.views.places import *  # nopep8
from api.v1.views.places_reviews import *  # nopep8
from api.v1.views.places_amenities import *  # nopep8
