from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by current emotion."""
        intensity = ""
        if self.emotion > 0.7:
            intensity = " z močno strastjo"
        elif self.emotion > 0.3:
            intensity = " s pridihom čustev"

        if self.state == "Ego":
            return f"Verjamem{intensity}, da je resnica absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"Spoznal sem{intensity}, da je resnica relativna, oblikovana z našimi odnosi."
        return f"Uvidel sem{intensity}, da so vse resnice eno, medsebojno povezane."
