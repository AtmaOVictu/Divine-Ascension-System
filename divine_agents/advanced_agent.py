from __future__ import annotations
from typing import List, Optional

from .agent import Agent


class MultiLayeredAgent(Agent):
    """Agent with additional loyalty and experience layers for transitions."""

    def __init__(self,
                 name: str,
                 state: str = "Ego",
                 tension: float = 0.0,
                 emotion: float = 0.0,
                 loyalty: float = 0.5,
                 experiences: Optional[List[str]] = None,
                 emotion_label: str = "neutral") -> None:
        super().__init__(name, state, tension, emotion)
        self.loyalty = loyalty
        self.experiences = experiences or []
        self.emotion_label = emotion_label

    def multi_layer_transition(self) -> str:
        """Handle more nuanced state transitions using loyalty and experiences."""
        emotion_layer = self.emotion
        tension_layer = self.tension
        loyalty_layer = self.loyalty
        experience_layer = self.experiences[-1] if self.experiences else "neutral"

        if self.state == "Ego" and (tension_layer > 0.7 or emotion_layer > 0.5 or self.emotion_label == "fearful"):
            self.state = "Jaz"
        elif self.state == "Jaz" and (loyalty_layer > 0.8 or "selfish" in experience_layer):
            self.state = "Enotnost"

        self.history.append(self.state)
        return self.state
