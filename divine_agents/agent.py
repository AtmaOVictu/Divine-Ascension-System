"""Core agent logic used throughout the project."""

from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of transitioning between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = value
        self.tension = min(1.0, self.tension + value)

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

    def philosophy(self) -> str:
        """Return the philosophical stance for the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotion."""
        base = self.philosophy()
        if self.emotion > 0.5:
            return f"{base} (čustvo intenziteta {self.emotion:.2f})"
        return base
