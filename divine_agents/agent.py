from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=lambda: ["Ego"])

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
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            prefix = "Z jezo" if self.emotion > 0.6 else "Mirno"
            return f"{prefix} trdim, da je resnica absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            prefix = "S sočutjem" if self.emotion > 0.6 else "Premišljeno"
            return f"{prefix} menim, da je resnica relativna, oblikovana z našimi odnosi."
        prefix = "V radosti" if self.emotion > 0.6 else "V harmoniji"
        return f"{prefix} verjamem, da so vse resnice eno, medsebojno povezane."
