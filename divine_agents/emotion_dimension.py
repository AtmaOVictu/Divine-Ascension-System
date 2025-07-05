"""Module defining an agent that links emotions with dimensions and senses."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


def _gaussian_integral(t: float, intensity: float) -> float:
    """Simple approximation of an integral used for emotion progression."""
    import math
    step = 0.01
    total = 0.0
    x = 0.0
    while x < t:
        total += math.exp(-((t - x) ** 2)) * step
        x += step
    return total * (intensity / 100)


@dataclass
class EmotionDimensionAgent:
    """Agent that tracks emotion intensity across dimensions and senses."""

    emotion: str
    intensity: float
    dimension: int
    senses: Dict[str, float] = field(default_factory=dict)

    def activate(self) -> None:
        """Activate emotion processing and adjust senses."""
        print(
            f"Čustvo '{self.emotion}' z intenzivnostjo {self.intensity}% je aktivirano v dimenziji {self.dimension}."
        )
        self.process_emotion()

    def process_emotion(self) -> None:
        """Process emotion based on intensity and update sense perception."""
        if self.intensity > 50:
            print(f"Intenzivnost {self.emotion} je visoka, zaznana bo močna reakcija!")
        else:
            print(f"Intenzivnost {self.emotion} je zmerna, zaznana bo zmerna reakcija.")

        self.senses["touch"] = self.intensity * 0.5
        self.senses["sight"] = self.intensity * 0.4

        percentage_influence = (self.intensity / 100) * self.dimension
        print(
            f"Čustvo vpliva na zaznavo čutila: Dotik: {self.senses['touch']} | Vid: {self.senses['sight']}"
        )
        print(f"Delež čustva v tej dimenziji je: {percentage_influence * 100}%")


__all__ = ["EmotionDimensionAgent", "_gaussian_integral"]
