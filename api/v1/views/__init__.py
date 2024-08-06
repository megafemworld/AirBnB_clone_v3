#!/usr/bin/python3
"""initializing Blueprint """

from api.v1.views.index import *
from flask import Blueprint
from models.state import State
from api.v1.views.states import *
from models.city import City
from api.v1.views.cities import *
from models import storage
from models.amenity import Amenity
from api.v1.views.amenities import *
from api.v1.views.amenities import *
app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
