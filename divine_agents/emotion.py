class Emotion:
    """Represents an emotion with a bounded intensity."""

    def __init__(self, name: str, intensity: float = 0.0):
        self.name = name
        self.intensity = intensity

    def adjust(self, change: float) -> float:
        """Adjust intensity within [-1, 1]."""
        self.intensity += change
        if self.intensity > 1:
            self.intensity = 1
        elif self.intensity < -1:
            self.intensity = -1
        return self.intensity
