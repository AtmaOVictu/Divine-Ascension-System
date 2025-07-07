from __future__ import annotations

import random
from typing import List

from .agent import Agent


class VoiceAgent(Agent):
    """Agent that tracks mood and expresses responses with emotional tone."""

    TONES = {
        "anger": " (spoken with anger)",
        "fear": " (spoken with fear)",
        "joy": " (spoken with joy)",
        "neutral": " (spoken neutrally)",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, mood: str = "neutral") -> None:
        super().__init__(name, state, tension, emotion)
        self.mood = mood

    def update_emotion(self, mood: str, value: float) -> None:  # type: ignore[override]
        """Update mood and emotion intensity while adjusting tension."""
        self.mood = mood
        self.emotion = value
        if mood == "anger":
            self.tension += value
        elif mood == "joy":
            self.tension -= value
        elif mood == "fear":
            self.tension += value * 1.5
        else:
            self.tension += value / 2

    def _determine_tone(self) -> str:
        return self.TONES.get(self.mood, "")

    def respond(self, question: str) -> str:  # type: ignore[override]
        base = super().respond(question)
        return f"{base}{self._determine_tone()}"
