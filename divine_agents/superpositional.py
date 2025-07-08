"""Superpositional agent models for philosophical dialogue."""
from typing import List


class SuperpositionalAgent:
    """Agent capable of holding multiple states simultaneously."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, states: List[str] | None = None,
                 tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.states = states or ["Ego"]
        self.tension = tension
        self.emotion = emotion
        self.history = [self.states[0]]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _collapse(self) -> str:
        """Collapse superposed states into a single state."""
        if len(self.states) == 1:
            return self.states[0]
        if "Ego" in self.states and "Jaz" in self.states:
            return "Jaz"
        if "Jaz" in self.states and "Enotnost" in self.states:
            return "Enotnost"
        return self.states[0]

    def transition(self) -> str:
        """Transition based on collapsed state and thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            state = self._collapse()
            if state == "Ego":
                state = "Jaz"
            elif state == "Jaz":
                state = "Enotnost"
            self.states = [state]
        self.history.append(self.states[0])
        return self.states[0]

    def respond(self, question: str) -> str:
        """Generate philosophical response according to current state."""
        state = self.states[0]
        if state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
