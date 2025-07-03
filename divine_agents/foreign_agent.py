from __future__ import annotations

from typing import List, Tuple

from .agent import Agent


class ForeignInfluenceAgent(Agent):
    """Agent that adapts its emotional state based on foreign influences."""

    def __init__(
        self,
        name: str,
        filozofija: str,
        motivacija: str,
        dimenzija: str = "Ego",
        tension_threshold: float = 0.7,
        emotion_threshold: float = 0.5,
    ) -> None:
        super().__init__(name, state=dimenzija)
        self.filozofija = filozofija
        self.motivacija = motivacija
        self.tension_threshold = tension_threshold
        self.emotion_threshold = emotion_threshold
        self.ego_emotion = 0.5
        self.jaz_emotion = 0.5
        self.foreign_factors: List[Tuple[str, float]] = []
        self.log: List[str] = []
        self.reflections: List[str] = []

    def update_ego_emotion(self, value: float) -> None:
        """Update Ego emotion on a 0-1 scale and record the reflection."""
        if 0 <= value <= 1:
            self.ego_emotion = value
            self.log.append(f"{self.name} updated Ego Emotion to {value:.2f}")
            self.reflect_on_state()

    def update_jaz_emotion(self, value: float) -> None:
        """Update Jaz emotion on a 0-1 scale and record the reflection."""
        if 0 <= value <= 1:
            self.jaz_emotion = value
            self.log.append(f"{self.name} updated Jaz Emotion to {value:.2f}")
            self.reflect_on_state()

    def add_foreign_factor(self, factor: str, influence: float) -> None:
        """Register a foreign factor and adapt emotions accordingly."""
        self.foreign_factors.append((factor, influence))
        self.log.append(
            f"{self.name} detected foreign factor: {factor} ({influence:.2f})"
        )
        self.adapt_to_foreign_factors()

    def adapt_to_foreign_factors(self) -> None:
        """Adjust emotions depending on the average foreign influence."""
        if not self.foreign_factors:
            return

        avg = sum(val for _, val in self.foreign_factors) / len(self.foreign_factors)
        if avg > 0.7:
            self.update_jaz_emotion(min(1.0, self.jaz_emotion + 0.1))
        else:
            self.update_ego_emotion(max(0.0, self.ego_emotion - 0.1))

    def reflect_on_state(self) -> None:
        """Store a textual reflection on the agent's current focus."""
        if self.ego_emotion > self.jaz_emotion:
            reflection = f"{self.name} is focused on self-preservation (Ego)."
        elif self.jaz_emotion > self.ego_emotion:
            reflection = f"{self.name} is focused on collective well-being (Jaz)."
        else:
            reflection = f"{self.name} balances self and others."
        self.reflections.append(reflection)
        self.log.append(f"Reflection: {reflection}")

    def apply_transition(self) -> str:
        """Invoke the standard transition logic."""
        return self.transition()

    def report(self) -> str:
        """Return a textual log of events."""
        return "\n".join(self.log)
