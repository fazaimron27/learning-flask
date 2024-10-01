from flask import request, jsonify
from data import room_types, availability_rooms
from entities import RoomType, AvailabilityRoom


def room_types_with_availability():
    result = []
    for room_type in room_types:
        for availability in availability_rooms:
            if availability.room_type_id == room_type.room_type_id:
                result.append({
                    'room_type_name': room_type.room_type_name,
                    'date': availability.date,
                    'allotment': availability.allotment,
                    'price': availability.price
                })
    return jsonify(result)


def create_room_type():
    data = request.get_json()
    room_type = RoomType(
        room_type_id=len(room_types) + 1,
        room_type_name=data['room_type_name']
    )
    room_types.append(room_type)
    return jsonify({'message': 'Room type created successfully'}), 201


def modify_room_type(room_type_id):
    data = request.get_json()
    for room_type in room_types:
        if room_type.room_type_id == room_type_id:
            room_type.room_type_name = data['room_type_name']
            return jsonify({'message': 'Room type updated successfully'})
    return jsonify({'message': 'Room type not found'}), 404


def remove_room_type(room_type_id):
    global room_types
    room_types = [
        room_type for room_type in room_types if room_type.room_type_id != room_type_id]
    return jsonify({'message': 'Room type deleted successfully'})


def create_availability_room():
    data = request.get_json()
    availability_room = AvailabilityRoom(
        availability_id=len(availability_rooms) + 1,
        room_type_id=data['room_type_id'],
        date=data['date'],
        allotment=data['allotment'],
        price=data['price']
    )
    availability_rooms.append(availability_room)
    return jsonify({'message': 'Availability room created successfully'}), 201


def modify_availability_room(availability_id):
    data = request.get_json()
    for availability_room in availability_rooms:
        if availability_room.availability_id == availability_id:
            availability_room.room_type_id = data['room_type_id']
            availability_room.date = data['date']
            availability_room.allotment = data['allotment']
            availability_room.price = data['price']
            return jsonify({'message': 'Availability room updated successfully'})
    return jsonify({'message': 'Availability room not found'}), 404


def remove_availability_room(availability_id):
    global availability_rooms
    availability_rooms = [
        availability_room for availability_room in availability_rooms if availability_room.availability_id != availability_id]
    return jsonify({'message': 'Availability room deleted successfully'})
