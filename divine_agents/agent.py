"""Core functionality for ontological agents."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents a single agent within the ontological system.

    Attributes
    ----------
    name:
        Identifier for the agent.
    state:
        Current ontological state (``Ego``, ``Jaz`` or ``Enotnost``).
    tension:
        Accumulated tension within the agent.
    emotion:
        Current emotional intensity of the agent.
    history:
        List of states that the agent has transitioned through.
    """

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float) -> None:
        """Update the current emotion and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition the agent to the next state if thresholds are exceeded."""
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

    def speak(self, question: str) -> str:
        """Generate a dialogue line reflecting the agent's state."""
        answer = self.respond(question)
        return f"{self.name} ({self.state}): {answer}"
