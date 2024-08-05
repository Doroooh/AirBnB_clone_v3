!/usr/bin/python3
"""States views"""
from flask import jsonify, make_response, abort, request
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City


@app_views.route('/states/<id>/cities',
                 strict_slashes=False,
                 methods=['GET', 'POST'])
def view_cities_of_state(id):
    """Returns a list of all cities of a state, or delete a
    city if a given id
    """
    state = storage.get(State, id)

    if state is None:
        return abort(404)

    if request.method == 'GET':

        list = []
        for city in state.cities:
            list.append(city.to_dict())
        return jsonify(list)

        data.update({"state_id": id})

        # Create the object
        obj = City(**data)

        # Save the object in storage
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201


@app_views.route('/cities/<id>',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])

        storage.save()
        return jsonify(city.to_dict())
