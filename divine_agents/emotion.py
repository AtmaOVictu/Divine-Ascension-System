from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion with a type and intensity."""
    name: str
    intensity: float = 0.0

    def tension_effect(self) -> float:
        """Return how much tension this emotion contributes."""
        return self.intensity
