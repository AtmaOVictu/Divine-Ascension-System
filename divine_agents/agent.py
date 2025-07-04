from __future__ import annotations

import math


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        """Initialize the agent with a starting state, tension and emotion."""
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

    # --------------------------
    # Transition mechanics
    # --------------------------

    def calculate_progress(self, t: float) -> float:
        """Return sigmoid-based progress for smooth transitions."""
        return 1 / (1 + math.exp(-t))

    def evolve(self, t: float) -> str:
        """Evolve state based on a time parameter using emotional progress."""
        progress = self.calculate_progress(t)
        if progress > 0.7:
            self.state = "Jaz"
        if progress > 0.9:
            self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

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
        """Return a philosophical answer depending on the current state."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Čutim močna čustva, kar poglablja moj pogled."
        return base
