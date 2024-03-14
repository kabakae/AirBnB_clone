#!/usr/bin/python3
"""Defines the town class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represents a Town.


    Attributes:
        Town_id (str): The town id.
        user_id (str): The User id.
        name (str): The name of the Town.
        despcription (str): Despcription of the place.
        number_rooms (int): Number of rooms in the town.
        number_bathrooms (int): Number of rooms bathrooms of the place.
        max_guest (int): The maximum number of guest in all rooms.
        latitude (float): The latitude of the area.
        longitude (float): The Longtitude of the area.
        amenities_ids (list): A list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
