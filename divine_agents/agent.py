"""Agent models used for philosophical state transitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict


TENSION_THRESHOLD = 0.7
EMOTION_THRESHOLD = 0.5


class Agent:
    """Represent an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
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

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > TENSION_THRESHOLD or self.emotion > EMOTION_THRESHOLD:
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

    def philosophical_view(self) -> str:
        """Short statement describing the agent's current view of truth."""
        return self.respond("Kaj je resnica?")


class MultiDimensionalAgent(Agent):
    """Agent with additional dimensions influencing transitions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.dimensions: Dict[str, float] = {"time": 0.0, "space": 0.0}

    def update_dimension(self, dimension: str, value: float) -> None:
        self.dimensions[dimension] = value

    def transition(self) -> str:  # type: ignore[override]
        if self.dimensions.get("emotion", self.emotion) > EMOTION_THRESHOLD:
            self.state = "Jaz" if self.state == "Ego" else "Enotnost"
        return super().transition()
