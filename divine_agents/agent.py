"""Core agent logic for the ontological system."""

from __future__ import annotations

from typing import Union


EMOTION_VALUES = {
    "fear": -1j,
    "anger": -1.2j,
    "sorrow": -0.8j,
    "joy": 0.8,
    "love": 1.0,
    "neutral": 0.0,
}


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Union[float, complex] = 0.0,
                 emotion_name: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Union[float, complex] = emotion
        self.emotion_name = emotion_name
        self.history = [state]

    def update_emotion(self, value: Union[str, float, complex]) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        if isinstance(value, str):
            self.emotion_name = value
            val = EMOTION_VALUES.get(value, 0.0)
        else:
            val = value
        self.emotion = val
        self.tension += abs(val)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        """Return a philosophical answer influenced by the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        emotion_note = ""
        if isinstance(self.emotion, complex) and self.emotion.imag < 0:
            emotion_note = f" Počutim se {self.emotion_name}."
        elif isinstance(self.emotion, (int, float)) and self.emotion > 0:
            emotion_note = f" Počutim se {self.emotion_name}."
        return f"{base}{emotion_note}"
