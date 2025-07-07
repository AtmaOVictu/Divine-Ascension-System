"""Module implementing a self-aware agent capable of reflection."""
from __future__ import annotations
import time
from .agent import Agent
from .constants import Constants


class SelfAwareAgent(Agent):
    """An agent that can reflect on its state and emotion."""

    def __init__(self, name: str, state: str = "Ego", emotion_label: str = "joy",
                 tension: float = 0.0, emotion: float = 0.0) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.emotion_label = emotion_label
        self.timestamp = time.time()

    def reflect(self) -> str:
        """Return a reflection string describing the agent's state."""
        reflection = f"{self.name} is currently in {self.state} with emotion {self.emotion_label}."
        self.history.append(reflection)
        return reflection

    def transition(self) -> str:
        """Override to apply constant thresholds and update timestamp."""
        if Constants.is_tension_high(self.tension) or Constants.is_emotion_high(self.emotion):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        self.timestamp = time.time()
        return self.state

    def respond(self, question: str) -> str:
        """Generate a philosophical response including self-reflection."""
        base = super().respond(question)
        reflection = self.reflect()
        return f"{reflection} Response: {base}"
