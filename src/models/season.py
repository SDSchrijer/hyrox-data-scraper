# Standard Python package
from typing import Optional

# Internal modules
from src.models.event import Event

class Season:

    def __init__(
        self,
        name: str,
        year: str,
    ):
        """
        Constructor method.

        Args:
            year (str): _description_
            events (list): _description_
        """
        
        self.name = name
        self.events = []
        
    def add_event(self, event: Event):

        self.events.append(event)