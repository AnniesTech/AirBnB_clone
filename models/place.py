#!/usr/bin/python3
""" Class Place"""

from models.base_model import BaseModel


class Place(BaseModel):
    """Class Place"""

    city_id: str = ""  # it will be the City.id
    user_id: str = ""  # it will be the User.id
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []  # will be the list of Amenity.id later
