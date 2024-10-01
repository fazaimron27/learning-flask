from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration purposes
room_types = [
    {"room_type_id": 1, "room_type_name": "Deluxe"},
    {"room_type_id": 2, "room_type_name": "Junior"},
    {"room_type_id": 3, "room_type_name": "President"},
]

availability_rooms = [
    {"availability_id": 1, "room_type_id": 3,
        "date": "27-9-2024", "allotment": 4, "price": 1808000},
    {"availability_id": 2, "room_type_id": 2,
        "date": "27-9-2024", "allotment": 2, "price": 1000000},
    {"availability_id": 3, "room_type_id": 1,
        "date": "27-9-2024", "allotment": 64, "price": 680000}
]


@app.route('/room_types_with_availability', methods=['GET'])
def room_types_with_availability():
    result = []
    for room_type in room_types:
        for availability in availability_rooms:
            if availability['room_type_id'] == room_type['room_type_id']:
                result.append({
                    'room_type_name': room_type['room_type_name'],
                    'date': availability['date'],
                    'allotment': availability['allotment'],
                    'price': availability['price']
                })
    return jsonify(result)


@app.route('/room_type', methods=['POST'])
def create_room_type():
    data = request.get_json()
    room_type = {
        'room_type_id': len(room_types) + 1,
        'room_type_name': data['room_type_name']
    }
    room_types.append(room_type)
    return jsonify({'message': 'Room type created successfully'}), 201


@app.route('/room_type/<int:room_type_id>', methods=['PUT'])
def modify_room_type(room_type_id):
    data = request.get_json()
    for room_type in room_types:
        if room_type['room_type_id'] == room_type_id:
            room_type['room_type_name'] = data['room_type_name']
            return jsonify({'message': 'Room type updated successfully'})
    return jsonify({'message': 'Room type not found'}), 404


@app.route('/room_type/<int:room_type_id>', methods=['DELETE'])
def remove_room_type(room_type_id):
    global room_types
    room_types = [
        room_type for room_type in room_types if room_type['room_type_id'] != room_type_id]
    return jsonify({'message': 'Room type deleted successfully'})


@app.route('/availability_room', methods=['POST'])
def create_availability_room():
    data = request.get_json()
    availability_room = {
        'availability_id': len(availability_rooms) + 1,
        'room_type_id': data['room_type_id'],
        'date': data['date'],
        'allotment': data['allotment'],
        'price': data['price']
    }
    availability_rooms.append(availability_room)
    return jsonify({'message': 'Availability room created successfully'}), 201


@app.route('/availability_room/<int:availability_id>', methods=['PUT'])
def modify_availability_room(availability_id):
    data = request.get_json()
    for availability_room in availability_rooms:
        if availability_room['availability_id'] == availability_id:
            availability_room['room_type_id'] = data['room_type_id']
            availability_room['date'] = data['date']
            availability_room['allotment'] = data['allotment']
            availability_room['price'] = data['price']
            return jsonify({'message': 'Availability room updated successfully'})
    return jsonify({'message': 'Availability room not found'}), 404


@app.route('/availability_room/<int:availability_id>', methods=['DELETE'])
def remove_availability_room(availability_id):
    global availability_rooms
    availability_rooms = [
        availability_room for availability_room in availability_rooms if availability_room['availability_id'] != availability_id]
    return jsonify({'message': 'Availability room deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
