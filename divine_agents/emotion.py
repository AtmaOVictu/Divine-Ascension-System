class Emotion:
    """Represents an emotional state with a name and intensity."""

    def __init__(self, name: str = "neutral", intensity: float = 0.0):
        self.name = name
        self.intensity = self._clamp(intensity)

    def _clamp(self, value: float) -> float:
        return max(-1.0, min(1.0, value))

    def change_intensity(self, change: float) -> None:
        """Change intensity but keep within [-1, 1]."""
        self.intensity = self._clamp(self.intensity + change)

    def set_intensity(self, value: float) -> None:
        self.intensity = self._clamp(value)

    def transition(self, new_emotion: "Emotion") -> None:
        """Transition to a new emotional state."""
        self.name = new_emotion.name
        self.intensity = self._clamp(new_emotion.intensity)

    def __repr__(self) -> str:
        return f"Emotion(name={self.name!r}, intensity={self.intensity})"
