from dataclasses import dataclass

@dataclass
class Emotion:
    """Simple representation of an emotion and its intensity."""
    kind: str = "neutral"
    intensity: float = 0.0

    def influence(self) -> float:
        """Return how much the emotion contributes to tension."""
        return self.intensity
