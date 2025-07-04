from __future__ import annotations
from .emotion import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history = [state]

    def update_emotion(self, emotion: Emotion) -> None:
        """Update emotion components and adjust tension accordingly."""
        self.emotion = emotion
        self.tension += emotion.value()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.value() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        mood = "Čustveno, " if self.emotion.value() > 0.5 else "Mirno, "
        if self.state == "Ego":
            return mood + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return mood + "Resnica je relativna, oblikovana z našimi odnosi."
        return mood + "Vse resnice so eno, medsebojno povezane."
