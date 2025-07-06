"""Ontology driven agent model used in the tests.

The :class:`Agent` class encapsulates the minimal behaviour required by the
unit tests.  It keeps track of ``emotion`` and ``tension`` levels and allows the
agent to transition between ontological states (``Ego``, ``Jaz`` and
``Enotnost``) once the appropriate thresholds are met.

Transitions are triggered when either ``tension`` exceeds ``0.7`` or ``emotion``
is above ``0.5``.  ``update_emotion`` also increases the current ``tension`` so
that emotions can gradually push an agent towards the next state.
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of changing states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Update the agent's emotional level.

        The provided ``value`` becomes the current emotional intensity and is
        also added to ``tension`` to reflect that stronger emotions usually
        increase tension within the agent.
        """
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the ``tension`` level."""
        self.tension = value

    def transition(self) -> str:
        """Transition to the next state when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on the current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
