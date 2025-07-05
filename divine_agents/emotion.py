"""Emotion management utilities."""

from dataclasses import dataclass

@dataclass
class Emotion:
    label: str
    intensity: float = 0.0

    def update(self, label: str, intensity: float) -> None:
        """Update emotion with a new label and intensity."""
        self.label = label
        self.intensity = intensity
