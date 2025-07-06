from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotion affecting an agent."""
    kind: str = "neutral"
    intensity: float = 0.0

    def escalate(self, delta: float) -> None:
        """Increase emotion intensity and cap at 1.0."""
        self.intensity = min(1.0, self.intensity + delta)
