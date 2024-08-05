#!/usr/bin/python3
''' new view for State objects'''

from flask import Flask
from flask import Flask, abort
from api.v1.views import app_views
from os import name
from models.state import State
from flask import request


@app_views.route('/status', methods=['GET'] strict_slashes=False)
def toGet():
    '''getting thing'''
    objects = storage.all('State')
    lista = []
    for state in objects.values():
        lista.append(state.to_dict())
    return jsonify(lista)
