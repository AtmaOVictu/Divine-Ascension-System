from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state with a type and intensity."""
    type: str
    intensity: float = 0.0
