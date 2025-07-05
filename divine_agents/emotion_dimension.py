"""Emotion and dimension interaction module."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class EmotionDimensionAgent:
    """Represents an emotion acting within a dimension and its sensory impact."""

    emotion: str
    intensity: float
    dimension: int
    senses: Dict[str, float] = field(default_factory=dict)

    def activate(self) -> str:
        """Activate the emotion within the dimension and return summary."""
        influence = self.process_emotion()
        return (
            f"Čustvo '{self.emotion}' z intenzivnostjo {self.intensity}% "
            f"je aktivirano v dimenziji {self.dimension}. Delež vpliva: {influence * 100:.1f}%"
        )

    def process_emotion(self) -> float:
        """Calculate sensory influence and return overall influence factor."""
        self.senses["touch"] = self.intensity * 0.5
        self.senses["sight"] = self.intensity * 0.4
        return (self.intensity / 100) * self.dimension
