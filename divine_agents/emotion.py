from dataclasses import dataclass


@dataclass
class Emotion:
    """Model emotion as E/M/O/T/I0N components."""

    energy: float = 0.0
    motivation: float = 0.0
    feeling: str = ""
    tension: float = 0.0
    intensity: float = 0.0
    potential: float = 0.0

    def as_intensity(self) -> float:
        """Return the current intensity level."""
        return self.intensity
