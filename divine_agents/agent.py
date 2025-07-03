"""Agent definitions for the Divine-Ascension-System.

This module provides a simple agent model used to explore philosophical
state transitions. Agents move between the states ``Ego``, ``Jaz`` and
``Enotnost`` based on their emotional intensity and internal tension.
The software is distributed under the MIT License. See ``LICENSE`` for
details.
"""

from dataclasses import dataclass, field
from typing import List


THRESHOLD_TENSION = 0.7
THRESHOLD_EMOTION = 0.5


@dataclass
class Agent:
    """Represent an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(init=False)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history = [self.state]

    def update_emotion(self, value: float) -> None:
        """Update emotion and accumulate tension."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state if thresholds are exceeded."""
        if self.tension > THRESHOLD_TENSION or self.emotion > THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, _question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
