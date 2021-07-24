from typing import Dict, Optional
from enum import Enum, auto
from dataclasses import dataclass

from .mapsite import MapSite


class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()


@dataclass
class Room(MapSite):

    roomNumber: int
    sides: Optional[Dict[Direction, MapSite]] = None

    def setSide(self, direction: Direction, side: MapSite):
        self.sides[direction] = side

    def getSide(self, direction: Direction) -> MapSite:
        return self.sides.get(direction, None)

    def enter(self):
        print("Entering next room")
