class Emotion:
    """Simple representation of an emotion with label and intensity."""

    def __init__(self, label: str = "neutral", intensity: float = 0.0):
        self.label = label
        self.intensity = intensity

    def update(self, label: str, intensity: float) -> None:
        self.label = label
        self.intensity = intensity

    def __repr__(self) -> str:
        return f"Emotion(label={self.label!r}, intensity={self.intensity})"
