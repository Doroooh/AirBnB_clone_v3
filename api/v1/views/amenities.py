#!/usr/bin/python3
"""Amenity module"""
from flask import jsonify, abort, request, make_response
from flasgger.utils import swag_from

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
@swag_from('documentation/amenity/get.yml', methods=['GET'])
def get_amenities():
    """Retrieve all Amenity objects"""
    all_amenities = [obj.to_dict() for obj in storage.all(Amenity).values()]
    return jsonify(all_amenities)


@app_views.route('/amenities/<string:amenity_id>', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/amenity/get_id.yml', methods=['GET'])
def get_amenity(amenity_id):
    """Retrieve amenity by id"""
    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<string:amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/amenity/delete.yml', methods=['DELETE'])
def delete_amenity(amenity_id):
    """Deletes a Amenity object by id"""
    amenity = storage.get(Amenity, amenity_id)

    if amenity is None:
        abort(404)

    amenity.delete()
    storage.save()
    return jsonify({})


@app_views.route('/amenities/', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/amenity/post.yml', methods=['POST'])
def create_amenity():
    """Creates Amenity object"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    if 'name' not in request.get_json():
        return make_response(jsonify({"error": "Missing name"}), 400)

    json_obj = request.get_json()
    obj = Amenity(**json_obj)
    obj.save()
    return (jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<string:amenity_id>', methods=['PUT'],
                 strict_slashes=False)
@swag_from('documentation/amenity/put.yml', methods=['PUT'])
def update_amenity(amenity_id):
    """Updates Amenity object"""
    if not request.get_json():
        return make_response(jsonify({"error": "Not a JSON"}), 400)

    obj = storage.get(Amenity, amenity_id)

    if obj is None:
        abort(404)

    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(obj, key, value)

    storage.save()
    return jsonify(obj.to_dict())
