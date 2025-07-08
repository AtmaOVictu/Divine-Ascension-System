"""Ontological agents capable of emotional state transitions."""

from __future__ import annotations

import math


class Agent:
    """Represents an ontological agent with emotion and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def decay_tension(self, time_step: float = 1.0) -> None:
        """Decay tension exponentially based on the current emotional level."""
        decay_rate = 0.1 + self.emotion * 0.3
        self.tension *= math.exp(-decay_rate * time_step)

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def philosophical_answer(self) -> str:
        """Return an emotionally influenced philosophical answer."""
        base = self.respond("Kaj je resnica?")
        if self.emotion > 0.7:
            prefix = "Z veliko strasti trdim: "
        elif self.emotion < 0.3:
            prefix = "Mirno pravim: "
        else:
            prefix = ""
        return f"{prefix}{base}"
