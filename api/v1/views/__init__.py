#!/usr/bin/python3
"""initializing Blueprint """

from flask import Blueprint


app_views = Bluprint('app_views', __name__, url_prefix="/api/v1")


from api.v1.views.index import *
