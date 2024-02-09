#!/usr/bin/python3
"""defines the state class."""
from models.base_model import BaseModel


class State(BaseModel):
    """represent a state.

    attributes:
        name (str): The name of the state.
    """

    name = ""
