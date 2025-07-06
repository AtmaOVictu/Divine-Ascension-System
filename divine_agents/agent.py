"""Core agent model representing ontological and emotional state."""

from dataclasses import dataclass, field
from enum import Enum
from typing import List


class OntologicalState(Enum):
    """Enumerates possible states of being."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Emotion(Enum):
    """Basic emotions influencing tension."""

    FEAR = "strah"
    JOY = "veselje"
    ANGER = "jeza"
    NEUTRAL = "brezcutno"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion: Emotion = Emotion.NEUTRAL
    history: List[OntologicalState] = field(default_factory=lambda: [OntologicalState.EGO])

    def update_emotion(self, emotion: Emotion, level: float) -> None:
        """Update emotion type and intensity, adjusting tension."""

        self.emotion = emotion
        self.emotion_level = level
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = value

    def transition(self) -> OntologicalState:
        """Perform state transition when thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str | None = None) -> str:
        """Return a philosophical answer influenced by state and emotion."""

        if self.state == OntologicalState.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == OntologicalState.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion != Emotion.NEUTRAL:
            base += f" Občutim {self.emotion.value}."

        return base
