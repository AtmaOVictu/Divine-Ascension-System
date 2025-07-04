from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of state transitions and responses."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: List[str] = field(init=False)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history = [self.state]

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
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

    def _mood(self) -> str:
        """Return a word describing the agent's current mood."""
        if self.emotion > 0.8:
            return "navdu\u0161eno"
        if self.emotion > 0.5:
            return "strastno"
        if self.emotion > 0.2:
            return "mirno"
        return "ravnodu\u0161no"

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and mood."""
        mood = self._mood()
        if self.state == "Ego":
            text = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            text = "Resnica je relativna, oblikovana z na\u0161imi odnosi."
        else:
            text = "Vse resnice so eno, medsebojno povezane."
        return f"{text} ({mood})"
