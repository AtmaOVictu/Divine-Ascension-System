from dataclasses import dataclass

@dataclass
class Emotion:
    """Simple representation of an emotion and its intensity."""
    name: str
    level: float
