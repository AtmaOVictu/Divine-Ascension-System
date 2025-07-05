from dataclasses import dataclass

@dataclass
class Emotion:
    """Simple emotion representation with intensity in [-1, 1]."""
    name: str
    intensity: float

    def change(self, delta: float) -> float:
        """Change the intensity within the allowed range."""
        self.intensity = max(-1.0, min(1.0, self.intensity + delta))
        return self.intensity
