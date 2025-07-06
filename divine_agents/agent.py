"""Core primitives for the Divine Ascension system."""

from __future__ import annotations

import random


class Agent:
    """Ontological agent capable of transitioning between philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, *, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, environment: str = "harmonious"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.environment = environment
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
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the agent's emotion."""
        mood = "strastno" if self.emotion > 0.6 else "mirno"
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} ({mood})"

    def simulate_environment(self) -> str:
        """Adjust emotional state based on environment and transition."""
        if self.environment == "harmonious":
            self.update_emotion(0.3)
            self.update_tension(0.4)
        elif self.environment == "disharmonious":
            self.update_emotion(0.7)
            self.update_tension(1.2)
        else:
            self.update_emotion(random.uniform(0.1, 0.5))
            self.update_tension(random.uniform(0.1, 0.5))
        return self.transition()
