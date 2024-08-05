#!/usr/bin/python3

"""index of the views"""
from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def status_api():
    """API status"""
    return jsonify({"status": "OK"})
