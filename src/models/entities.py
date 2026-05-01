from dataclasses import dataclass
from enum import Enum
from typing import List, Tuple
import uuid

class ObjectState(Enum):
    DETECTED = "DETECTED"
    IN_TRANSIT = "IN_TRANSIT"
    SORTED = "SORTED"
    ERROR = "ERROR"

@dataclass
class SortingBin:
    id: str
    accepted_category: str
    location: Tuple[float, float, float]

@dataclass
class Object:
    color_category: str
    size_class: str
    coordinates: Tuple[float, float, float]
    state: ObjectState = ObjectState.DETECTED
    id: str = str(uuid.uuid4())

@dataclass
class Workspace:
    pickup_zone: Tuple[float, float, float, float]  # x_min, x_max, y_min, y_max
    bins: List[SortingBin]
    home_position: Tuple[float, float, float]
