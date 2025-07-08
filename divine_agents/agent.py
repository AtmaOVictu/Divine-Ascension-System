from __future__ import annotations
from typing import Optional
from .emotion import Emotion
from .karma import Karma


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: Optional[Emotion] = None, karma: Optional[Karma] = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.karma = karma or Karma()
        self.history = [state]

    def update_emotion(self, **kwargs) -> None:
        """Update emotional values and adjust tension."""
        for key, val in kwargs.items():
            if hasattr(self.emotion, key):
                setattr(self.emotion, key, val)
        self.tension += self.emotion.intensity()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        self.karma.update(self.emotion)
        if self.tension > 0.7 or self.emotion.intensity() > 0.5:
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
