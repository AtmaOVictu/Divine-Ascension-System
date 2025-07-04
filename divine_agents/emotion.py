from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents emotion decomposed into E/M/O/T/I0N components."""
    energy: float = 0.0  # E
    motivation: float = 0.0  # M
    feeling: float = 0.0  # O
    tension: float = 0.0  # T
    intensity: float = 0.0  # I
    potential: float = 0.0  # 0
    navigation: float = 0.0  # N

    def value(self) -> float:
        """Return the maximum intensity among components."""
        return max(
            self.energy,
            self.motivation,
            self.feeling,
            self.tension,
            self.intensity,
            self.potential,
            self.navigation,
        )
