"""Ontological agent able to transition through philosophical states."""

from typing import List


STATE_PRINCIPLES = {
    "Ego": "Resnica je absolutna in neodvisna od drugih.",
    "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
    "Enotnost": "Vse resnice so eno, medsebojno povezane.",
}

STATE_SYMBOLS = {
    "Ego": "⊘",
    "Jaz": "∫(dru/x)",
    "Enotnost": "RES001",
}


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]

    def __repr__(self) -> str:
        return f"Agent(name={self.name}, state={self.state}, tension={self.tension}, emotion={self.emotion})"

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    @property
    def symbol(self) -> str:
        """Return the symbol associated with the current state."""
        return STATE_SYMBOLS.get(self.state, "")

    def transition(self) -> str:
        """Perform state transition if emotion > 0.5 or tension > 0.7."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        return STATE_PRINCIPLES.get(self.state, "")
