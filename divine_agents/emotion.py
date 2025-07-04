from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents the E/M/O/T/I0N emotional framework."""

    energy: float = 0.0
    motivation: float = 0.0
    feeling: float = 0.0
    tension: float = 0.0
    intensity: float = 0.0
    potential: float = 0.0
    navigation: float = 0.0

    @property
    def value(self) -> float:
        """Return overall emotional intensity."""
        total = (
            self.energy
            + self.motivation
            + self.feeling
            + self.tension
            + self.intensity
            + self.potential
            + self.navigation
        )
        return total / 7
