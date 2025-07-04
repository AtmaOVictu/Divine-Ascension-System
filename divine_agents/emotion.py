from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotional state."""
    kind: str = "neutral"
    intensity: float = 0.0

    def update(self, kind: str, intensity: float) -> None:
        self.kind = kind
        self.intensity = intensity
