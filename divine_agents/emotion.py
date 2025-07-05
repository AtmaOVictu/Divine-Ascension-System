from dataclasses import dataclass


@dataclass
class Emotion:
    """Simple representation of an emotion with a name and intensity."""

    name: str
    intensity: float = 0.0
