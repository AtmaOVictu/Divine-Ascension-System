from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state."""
    name: str
    intensity: float
