#!/usr/bin/python3
"""States views"""
from flask import jsonify, make_response, abort, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities',
                 strict_slashes=False,
                 methods=['GET', 'POST'])
def view_amenities():
    """Returns the list of all Amenity objects"""
    if request.method == 'POST':

        # Get the attributes from the request
        data = request.get_json()

        if isinstance(data, dict):
            pass
        else:
            return jsonify({"error": "Not a JSON"}), 400

        if 'name' not in data.keys():
            return jsonify({'error': 'Missing name'}), 400

        # Create the object
        obj = Amenity(**data)

        # Save the object in storage
        storage.new(obj)
        storage.save()
        return jsonify(obj.to_dict()), 201



@app_views.route('/amenities/<id>',
                 strict_slashes=False,
                 methods=['GET', 'DELETE', 'PUT'])

        storage.save()
        return jsonify(amenity.to_dict())
