from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion with a name and intensity."""
    name: str
    intensity: float

    def impact_on_tension(self) -> float:
        """Return the tension change caused by this emotion."""
        return self.intensity
