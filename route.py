from flask import Blueprint
from handler import (
    room_types_with_availability,
    create_room_type,
    modify_room_type,
    remove_room_type,
    create_availability_room,
    modify_availability_room,
    remove_availability_room
)

room_type_blueprint = Blueprint('room_type', __name__)
availability_room_blueprint = Blueprint('availability_room', __name__)


@room_type_blueprint.route('/room_types_with_availability', methods=['GET'])
def room_types_with_availability_route():
    return room_types_with_availability()


@room_type_blueprint.route('/room_type', methods=['POST'])
def create_room_type_route():
    return create_room_type()


@room_type_blueprint.route('/room_type/<int:room_type_id>', methods=['PUT'])
def modify_room_type_route(room_type_id):
    return modify_room_type(room_type_id)


@room_type_blueprint.route('/room_type/<int:room_type_id>', methods=['DELETE'])
def remove_room_type_route(room_type_id):
    return remove_room_type(room_type_id)


@availability_room_blueprint.route('/availability_room', methods=['POST'])
def create_availability_room_route():
    return create_availability_room()


@availability_room_blueprint.route('/availability_room/<int:availability_id>', methods=['PUT'])
def modify_availability_room_route(availability_id):
    return modify_availability_room(availability_id)


@availability_room_blueprint.route('/availability_room/<int:availability_id>', methods=['DELETE'])
def remove_availability_room_route(availability_id):
    return remove_availability_room(availability_id)
