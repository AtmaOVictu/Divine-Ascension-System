"""Ontological agents capable of philosophical state transitions."""

from __future__ import annotations

import uuid


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]
        self.id = self.generate_id()

    # ------------------------------------------------------------------
    # Basic state and emotion management
    # ------------------------------------------------------------------

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def generate_id(self) -> str:
        """Create a unique identifier for this agent."""
        return f"{self.name}_{uuid.uuid4().hex[:8]}"

    def emotion_prefix(self) -> str:
        """Return a short textual cue based on emotion intensity."""
        return "vznemirjeno" if self.emotion > 0.5 else "mirno"

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
        base: str
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        prefix = self.emotion_prefix().capitalize()
        return f"{prefix} odgovarjam: {base}"

    # ------------------------------------------------------------------
    # Reflection utilities
    # ------------------------------------------------------------------

    def replay_history(self) -> str:
        """Return the chronological history of states."""
        return " -> ".join(self.history)

    def copy_state(self) -> "Agent":
        """Create a duplicate of the current agent."""
        return Agent(self.name, self.state, self.tension, self.emotion)

    def mark_with_tattoo(self, tattoo: str) -> None:
        """Record a significant permanent event."""
        self.history.append(f"Tattoo:{tattoo}")
