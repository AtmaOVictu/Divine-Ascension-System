"""Ontology based multi colour agent implementation."""

import random
from typing import List


class Agent:
    """Represents an ontological agent capable of transitioning states.

    Each agent carries a colour representation of its current ontological
    state and may expose or hide this colour (``visibility``).  State
    transitions are governed by emotion and tension thresholds.
    """

    STATES = ("Ego", "Jaz", "Enotnost")
    COLOURS = {
        "Ego": "Red",
        "Jaz": "Blue",
        "Enotnost": "Gold",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name: str = name
        self.state: str = state
        self.tension: float = tension
        self.emotion: float = emotion
        self.history: List[str] = [state]
        self.colour: str = self.COLOURS[state]
        self.visibility: str = "Hidden"

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotions directly contribute to tension build-up
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _update_colour(self) -> None:
        """Synchronise colour with the current state."""
        self.colour = self.COLOURS[self.state]

    def _toggle_visibility(self) -> None:
        """Randomly toggle colour visibility."""
        self.visibility = "Visible" if random.random() > 0.5 else "Hidden"

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self._update_colour()
            self._toggle_visibility()
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
