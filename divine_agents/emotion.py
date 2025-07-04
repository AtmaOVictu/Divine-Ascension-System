from dataclasses import dataclass


@dataclass
class Emotion:
    """Simple representation of an emotional state."""
    name: str
    intensity: float
