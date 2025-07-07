from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions and dialogue."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    identity: str = field(init=False)
    value: str = field(init=False)
    belief: str = field(init=False)
    history: List[str] = field(init=False, default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)
        self._update_philosophy()

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def _update_philosophy(self) -> None:
        """Internal helper to update identity, value and belief."""
        if self.state == "Ego":
            self.identity = "posameznik"
            self.value = "samostojnost"
            self.belief = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            self.identity = "relacijski jaz"
            self.value = "izkušnje skupnosti"
            self.belief = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            self.identity = "enotnost"
            self.value = "harmonija"
            self.belief = "Vse resnice so eno, medsebojno povezane."

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
        self._update_philosophy()
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        reply = self.belief
        if self.emotion > 0.5:
            reply += f" Čustveno to doživljam na ravni {self.emotion:.1f}."
        return reply
