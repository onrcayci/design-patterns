from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class MapSite(ABC):

    @abstractmethod
    def enter(self):
        pass
