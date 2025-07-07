"""Core logic for ontological agents and their state transitions."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional


class State(Enum):
    """Enumeration of ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Emotion(Enum):
    """Available emotional tones that influence tension."""

    FEAR = "strah"
    JOY = "veselje"
    ANGER = "jeza"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion_intensity: float = 0.0
    emotion_type: Optional[Emotion] = None
    history: List[State] = field(default_factory=lambda: [State.EGO])

    def update_emotion(self, emotion: Emotion, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion_type = emotion
        self.emotion_intensity = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_intensity > 0.5:
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

        if self.emotion_type == Emotion.FEAR:
            return f"{base} Čutim strah."
        if self.emotion_type == Emotion.JOY:
            return f"{base} Preveva me veselje."
        if self.emotion_type == Emotion.ANGER:
            return f"{base} Jezen sem."
        return base
