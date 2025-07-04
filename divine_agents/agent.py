"""Core agent functionality used throughout the Codex examples.

Each agent can exist in three ontological states:
```
Ego -> Jaz -> Enotnost
```
Transitions are triggered when either ``tension`` exceeds ``0.7`` or
``emotion`` exceeds ``0.5``.  The class stores a history of states so tests can
verify how the agent evolves during a dialogue.
"""

from __future__ import annotations

from enum import Enum


class OntologicalState(Enum):
    """Enumeration of supported philosophical states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(
        self,
        name: str,
        state: OntologicalState = OntologicalState.EGO,
        tension: float = 0.0,
        emotion: float = 0.0,
    ) -> None:
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

    def transition(self) -> OntologicalState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state is OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state is OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state is OntologicalState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state is OntologicalState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
