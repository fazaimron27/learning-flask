from entities import RoomType, AvailabilityRoom

room_types = [
    RoomType(room_type_id=1, room_type_name="Deluxe"),
    RoomType(room_type_id=2, room_type_name="Junior"),
    RoomType(room_type_id=3, room_type_name="President"),
]

availability_rooms = [
    AvailabilityRoom(availability_id=1, room_type_id=3,
                     date="27-9-2024", allotment=4, price=1808000),
    AvailabilityRoom(availability_id=2, room_type_id=2,
                     date="27-9-2024", allotment=2, price=1000000),
    AvailabilityRoom(availability_id=3, room_type_id=1,
                     date="27-9-2024", allotment=64, price=680000)
]
