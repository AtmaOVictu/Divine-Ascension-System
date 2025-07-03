from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Agent:
    """Ontological agent capable of transitioning between states.

    Parameters
    ----------
    name:
        Display name of the agent.
    state:
        Initial ontological state. One of ``Ego``, ``Jaz`` or ``Enotnost``.
    tension:
        Current tension level driving transitions.
    emotion:
        Current emotion intensity. This influences ``tension``.
    """

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list = field(default_factory=list)
    emotions: Dict[str, float] = field(default_factory=dict)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def set_emotion(self, name: str, intensity: float) -> None:
        """Set an emotion with a given intensity and update tension."""
        self.emotions[name] = intensity
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform a state transition if thresholds are exceeded."""
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
