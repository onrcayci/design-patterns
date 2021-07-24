from typing import Dict, Optional
from enum import Enum, auto

from .mapsite import MapSite


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


class Room(MapSite):

    roomNumber: int
    sides: Dict[Direction, MapSite]

    def setSide(self, direction: Direction, side: MapSite):
        self.sides[direction] = side

    def getSide(self, direction: Direction) -> MapSite:
        return self.sides.get(direction, None)
