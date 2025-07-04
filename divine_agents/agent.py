from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
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

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        prefix = "Strastno" if self.emotion > 0.7 else "Mirno" if self.emotion < 0.3 else ""

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix} {core}".strip()
