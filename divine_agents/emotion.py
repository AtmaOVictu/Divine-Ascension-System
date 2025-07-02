from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state with a type and intensity."""

    type: str
    intensity: float = 0.0

    def update(self, new_type: str, new_intensity: float) -> None:
        """Update emotion type and intensity."""
        self.type = new_type
        self.intensity = new_intensity

    def __str__(self) -> str:
        return f"{self.type.capitalize()} (intensity: {self.intensity})"
