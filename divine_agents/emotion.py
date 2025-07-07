from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotional state and its intensity."""

    kind: str
    intensity: float

    def __post_init__(self) -> None:
        # ensure intensity is non-negative
        if self.intensity < 0:
            raise ValueError("Intensity must be non-negative")
