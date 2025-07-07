"""Module implementing an ontological agent with state transitions."""

from __future__ import annotations

from uuid import uuid4


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [f"Start state: {state}"]
        self.id = self.generate_id()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Interaction methods
    # ------------------------------------------------------------------

    def reply(self, message: str) -> str:
        """Return a reply and record it in history."""
        answer = self.respond(message)
        self.history.append(f"{self.name} ({self.state}): {answer}")
        return answer

    # ------------------------------------------------------------------
    # Identity and history utilities
    # ------------------------------------------------------------------

    def generate_id(self) -> str:
        """Return a unique identifier for the agent."""
        return f"{self.name}-{uuid4()}"

    def mark_with_tattoo(self, tattoo: str) -> None:
        """Record a significant event in the agent's history."""
        self.history.append(f"Tattoo: {tattoo}")

    def copy_state(self) -> "Agent":
        """Create a copy of the agent preserving current state."""
        return Agent(self.name, self.state, self.tension, self.emotion)

    def replay_history(self) -> str:
        """Return the history log as a single string."""
        return "\n".join(self.history)

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
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
