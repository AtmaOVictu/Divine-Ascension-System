from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state with a type and intensity."""
    kind: str = "neutral"
    intensity: float = 0.0
