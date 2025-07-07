from __future__ import annotations
from typing import List
from .agent import Agent


class VoiceAgent(Agent):
    """Voice agent that handles emotions and tone in responses."""

    TONE_MAP = {
        "anger": " (spoken with anger)",
        "fear": " (spoken with fear)",
        "joy": " (spoken with joy)",
        "neutral": " (spoken neutrally)",
    }

    def __init__(self, name: str, state: str = "Ego", emotion: float = 0.0,
                 mood: str = "neutral") -> None:
        super().__init__(name, state=state, emotion=emotion)
        self.mood = mood
        self.tension = 0.0

    def update_emotion(self, mood: str, value: float) -> None:
        """Update mood and emotion, adjusting tension based on mood."""
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

    def respond(self, question: str) -> str:
        """Return philosophical answer influenced by mood."""
        response = super().respond(question)
        return response + self.TONE_MAP.get(self.mood, "")
