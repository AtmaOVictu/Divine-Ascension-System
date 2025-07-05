from __future__ import annotations

from typing import Dict

from .agent import Agent


class EmotionDimensionAgent(Agent):
    """Agent that also tracks dimension and senses during activation."""

    def __init__(self, name: str, dimension: int = 1, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name=name, state=state, tension=tension, emotion=emotion)
        self.dimension = dimension
        self.senses: Dict[str, float] = {}
        self.dimension_influence = 0.0

    def activate(self) -> None:
        """Activate emotion processing and potentially transition state."""
        print(
            f"\u010custvo '{self.emotion * 100:.0f}%', dimenzija {self.dimension} -- aktivacija"
        )
        self.process_emotion()
        self.transition()

    def process_emotion(self) -> None:
        """Calculate senses and dimension influence based on current emotion."""
        reaction = "močna" if self.emotion > 0.5 else "zmerna"
        print(f"Intenzivnost Čustva je {reaction}.")

        # compute senses influenced by emotion
        self.senses["touch"] = self.emotion * 0.5
        self.senses["sight"] = self.emotion * 0.4

        # dimension influence (percentage)
        self.dimension_influence = self.emotion * self.dimension
        print(
            f"Zaznava - dotik: {self.senses['touch']:.2f}, vid: {self.senses['sight']:.2f}"
        )
        print(f"Delež Čustva v dimenziji: {self.dimension_influence * 100:.2f}%")
