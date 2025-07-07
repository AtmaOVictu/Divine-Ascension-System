from dataclasses import dataclass

@dataclass
class EmotionState:
    """Hold intensities for different emotions."""
    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def update(self, name: str, value: float) -> None:
        if not hasattr(self, name):
            raise ValueError(f"Unknown emotion '{name}'")
        setattr(self, name, value)

    @property
    def overall(self) -> float:
        """Return maximum intensity across all emotions."""
        return max(self.fear, self.joy, self.anger)

    @property
    def tension_influence(self) -> float:
        """Average intensity used to influence tension."""
        return (self.fear + self.joy + self.anger) / 3
