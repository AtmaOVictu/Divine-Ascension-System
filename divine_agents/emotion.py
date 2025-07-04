from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion with a name and intensity."""

    name: str
    intensity: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.intensity <= 1.0:
            raise ValueError("Intensity must be between 0 and 1")
