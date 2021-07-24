from dataclasses import dataclass
from typing import Optional

from .mapsite import MapSite
from .room import Room


@dataclass
class Door(MapSite):

    isOpen: Optional[bool]
    roomFrom: Room
    roomTo: Room
