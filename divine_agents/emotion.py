from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotional state with an intensity."""

    name: str
    intensity: float = 0.0

    def contribution_to_tension(self) -> float:
        """Return how much this emotion contributes to tension."""
        return max(0.0, min(1.0, self.intensity))
