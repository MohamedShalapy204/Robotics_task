import json
from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class RobotConfig:
    serial_port: str = "/dev/ttyUSB0"
    baud_rate: int = 115200
    home_position: tuple = (0.0, 0.0, 0.0)
    workspace_limits: Dict[str, tuple] = field(default_factory=lambda: {
        "x": (-200, 200),
        "y": (100, 400),
        "z": (0, 300)
    })
    bins: Dict[str, tuple] = field(default_factory=lambda: {
        "red": (-150, 200, 50),
        "green": (0, 200, 50),
        "blue": (150, 200, 50)
    })

    def load_from_file(self, filepath: str):
        with open(filepath, 'r') as f:
            data = json.load(f)
            for k, v in data.items():
                if hasattr(self, k):
                    setattr(self, k, v)

settings = RobotConfig()
