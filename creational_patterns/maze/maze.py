from dataclasses import dataclass
from typing import Dict, Optional, Union

from .room import Room


@dataclass
class Maze:

    rooms: Optional[Dict[int, Room]]

    def addRoom(self, room: Room) -> None:
        self.rooms.append(room)

    def roomNo(self, number: int) -> Union[Room, None]:
        return self.rooms.get(number, None)
