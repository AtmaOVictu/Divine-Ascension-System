"""Core agent implementations for the Divine Ascension system."""

from __future__ import annotations

from typing import Dict, List, Optional
import random


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history: List[str] = [state]
        self.external_factors: Dict[str, float] = {}

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.history.append(f"Emotion set to {value}")

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.history.append(f"Tension set to {value}")

    def update_external_factor(self, factor: str, value: float) -> None:
        """Record an external factor influencing the agent."""
        self.external_factors[factor] = value
        self.history.append(f"External factor {factor}: {value}")

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            previous = self.state
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            if previous != self.state:
                self.history.append(f"Transitioned to {self.state}")
        else:
            self.history.append("No transition")
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        intensity = "mirno" if self.emotion < 0.3 else "strastno"
        if self.state == "Ego":
            return f"{intensity}, trdim da je resnica absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"{intensity}, verjamem, da je resnica relativna, oblikovana z našimi odnosi."
        return f"{intensity}, zaznavam, da so vse resnice eno, medsebojno povezane."
