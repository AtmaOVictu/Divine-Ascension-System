from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion with a type and intensity."""

    kind: str
    intensity: float

    def description(self) -> str:
        return f"{self.kind} (intensity {self.intensity:.1f})"
