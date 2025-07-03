"""Base classes and utilities for ontological agents."""

from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    PRINCIPLES = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
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

    @property
    def emotion_descriptor(self) -> str:
        """Return a textual description of the current emotional level."""
        if self.emotion > 0.7:
            return "veselje"
        if self.emotion > 0.5:
            return "vznemirjenje"
        if self.emotion > 0.3:
            return "nevtralno"
        return "mirnost"

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
        base = self.PRINCIPLES[self.state]
        if self.emotion > 0.7:
            base += "!"
        return base

    def talk(self, question: str) -> str:
        """Compose a dialogue line reflecting state and emotion."""
        answer = self.respond(question)
        return f"{self.name} ({self.state}, {self.emotion_descriptor}): {answer}"
