from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion using the E/M/O/T/I0N model."""

    energy: float = 0.0  # E - Energija
    motivation: float = 0.0  # M - Motivacija
    feeling: float = 0.0  # O - Občutek
    tension: float = 0.0  # T - Tenzija
    intensity: float = 0.0  # I - Intenzivnost
    potential: float = 0.0  # 0 - Potencial
    navigation: float = 0.0  # N - Navigacija

    def level(self) -> float:
        """Return overall intensity as average of all components."""
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

