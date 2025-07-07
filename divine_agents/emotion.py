from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state."""
    type: str
    intensity: float
