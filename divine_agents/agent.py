from __future__ import annotations
from typing import List
from .decision_maker import DecisionMaker


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, emotional_state: str = "neutral", *, state: str = "Ego", tension: float = 0.0, loyalty: float = 0.5) -> None:
        self.name = name
        self.state = state
        self.emotional_state = emotional_state
        self.tension = tension
        self.emotion = 0.0
        self.loyalty = loyalty
        self.belief_system: List[str] = []
        self.history = [state]
        self.decision_maker = DecisionMaker(self)

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and optionally change emotional label."""
        self.emotion = value
        if label:
            self.emotional_state = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition using the decision maker."""
        return self.decision_maker.decide_transition()

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
