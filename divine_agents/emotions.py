from dataclasses import dataclass

@dataclass
class Emotions:
    """Container for emotional states."""
    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    @property
    def intensity(self) -> float:
        """Return the strongest emotion intensity."""
        return max(self.fear, self.joy, self.anger)
