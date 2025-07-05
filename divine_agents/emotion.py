from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion with a name and intensity."""
    name: str
    intensity: float
