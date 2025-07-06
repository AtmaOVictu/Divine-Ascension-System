from dataclasses import dataclass, field
from enum import Enum
from typing import List


class State(Enum):
    """Possible ontological states of an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Emotion:
    """Represents an emotion with a given intensity."""

    name: str
    intensity: float


class Agent:
    """Ontological agent capable of changing states based on emotion and tension."""

    def __init__(self, name: str, state: State = State.EGO, tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion("neutral", 0.0)
        self.history: List[State] = [state]

    def update_emotion(self, emotion: Emotion) -> None:
        """Set a new emotion and adjust tension based on intensity."""
        self.emotion = emotion
        self.tension += emotion.intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == State.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == State.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
