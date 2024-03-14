#!/usr/bin/python3
"""Defines the Class location City."""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a location that in a city.

    Attributes:
        state_id (str): The unique city id.
        name (str): Name of the City.
    """


    state_id = ""
    name = ""
