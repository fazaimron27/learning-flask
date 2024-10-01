from dataclasses import dataclass


@dataclass
class RoomType:
    room_type_id: int
    room_type_name: str


@dataclass
class AvailabilityRoom:
    availability_id: int
    room_type_id: int
    date: str
    allotment: int
    price: int
