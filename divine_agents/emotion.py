from dataclasses import dataclass

@dataclass
class Emotion:
    """Simple emotion representation with type and intensity."""
    type: str
    intensity: float = 0.0
