from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion affecting an agent."""
    kind: str
    intensity: float = 0.0
