from __future__ import annotations

from typing import List

from .agent import Agent


class MultiLayerAgent(Agent):
    """Agent with additional layers and learning capabilities."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
        emotional_state: str = "neutral",
        experiences: List[str] | None = None,
    ) -> None:
        super().__init__(name, state, tension, emotion)
        self.loyalty = loyalty
        self.emotional_state = emotional_state
        self.experiences: List[str] = experiences or []

    def add_experience(self, exp: str) -> None:
        """Record a new experience."""
        self.experiences.append(exp)

    def adjust_tension_based_on_emotions(self) -> None:
        """Modify tension depending on current emotional state."""
        if self.emotional_state == "angry":
            self.tension += 0.3
        elif self.emotional_state == "happy":
            self.tension -= 0.2
        else:
            self.tension += 0.1

    def learn_from_past_decisions(self, situation: str) -> str:
        """Simple learning mechanism using last experiences."""
        if situation == "danger":
            if "helped" in self.experiences:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"

    def auto_refactor(self) -> str:
        """Adjust state based on historical patterns."""
        if "hesitation" in self.history:
            self.state = "Jaz"
        elif "self-preservation" in self.history:
            self.state = "Ego"
        return self.state

    def multi_layer_transition(self) -> str:
        """Transition based on multiple factors."""
        experience_layer = self.experiences[-1] if self.experiences else ""

        if self.emotional_state == "fearful" and self.tension > 0.7:
            self.state = "Ego"
        elif self.loyalty > 0.8 and self.emotional_state == "happy":
            self.state = "Jaz"
        elif "selfish" in experience_layer and self.tension > 0.5:
            self.state = "Enotnost"
        else:
            super().transition()
        self.history.append(self.state)
        return self.state
