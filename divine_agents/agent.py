from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(Enum):
    """Enumeration of possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Ontological agent capable of transitioning states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[State] = field(default_factory=lambda: [State.EGO])

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update emotion intensity and type, adjusting tension."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == State.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == State.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        if self.emotion_type != "neutral":
            base += f" (občuti {self.emotion_type})"
        return base
