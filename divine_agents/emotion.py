from dataclasses import dataclass

@dataclass
class Emotion:
    """Simple representation of an emotion with intensity."""
    name: str
    intensity: float

    def tension_effect(self) -> float:
        """Return how much this emotion contributes to tension."""
        return self.intensity
