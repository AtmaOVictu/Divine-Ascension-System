from __future__ import annotations

from typing import List

from .agent import Agent


class VoiceAgent(Agent):
    """Agent capable of responding with an emotional tone."""

    TONE_MAPPING = {
        "anger": " (spoken with anger)",
        "fear": " (spoken with fear)",
        "joy": " (spoken with joy)",
        "neutral": " (spoken neutrally)",
    }

    def __init__(self, name: str, state: str = "Ego", mood: str = "neutral", emotion: float = 0.0, tension: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.mood = mood

    def update_emotion(self, mood: str, value: float) -> None:  # type: ignore[override]
        """Update emotion and adjust tension according to mood."""
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

    def respond(self, question: str) -> str:  # type: ignore[override]
        base_response = super().respond(question)
        return base_response + self._determine_tone()

    def _determine_tone(self) -> str:
        return self.TONE_MAPPING.get(self.mood, " (spoken neutrally)")
