from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state with a name and intensity."""
    name: str
    intensity: float = 0.0

    def update(self, intensity: float) -> None:
        """Update intensity of the emotion."""
        self.intensity = intensity
