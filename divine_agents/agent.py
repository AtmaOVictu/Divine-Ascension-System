from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .environment import Environment

class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.values = set()
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def adapt_values(self, environment: 'Environment') -> None:
        """Modify values based on environmental influences."""
        if environment.societal_influence > 0.5:
            self.values.add("cooperation")
        if environment.natural_condition > 0.5:
            self.values.add("self-preservation")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def speak(self, question: str) -> str:
        """Generate a line of dialogue reflecting current state and emotion."""
        base = self.respond(question)
        if self.emotion > 0.5:
            feeling = "vznemirjeno"
        else:
            feeling = "mirno"
        return f"{self.name} ({self.state}, {feeling}): {base}"

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
