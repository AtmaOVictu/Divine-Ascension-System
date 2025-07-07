"""Core agent implementation for ontological state transitions."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional


class State(Enum):
    """Enumerates the possible ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class EmotionType(Enum):
    """Enumerates basic emotion types."""

    FEAR = auto()
    JOY = auto()
    ANGER = auto()


@dataclass
class Agent:
    """Represents an ontological agent capable of state transitions."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: Optional[EmotionType] = None
    history: List[State] = field(default_factory=lambda: [State.EGO])

    def update_emotion(self, e_type: EmotionType, level: float) -> None:
        """Set emotion type and level, adjusting tension."""

        self.emotion_type = e_type
        self.emotion_level = level
        self.tension += level

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""

        self.tension = value

    def transition(self) -> State:
        """Transition to the next state if thresholds are exceeded."""

        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self) -> str:
        """Return a philosophical statement based on current state and emotion."""

        if self.state == State.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == State.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        prefix = ""
        if self.emotion_type == EmotionType.ANGER:
            prefix = "Z jezo razmišljam, "
        elif self.emotion_type == EmotionType.FEAR:
            prefix = "S strahom povem, "
        elif self.emotion_type == EmotionType.JOY:
            prefix = "Z veseljem povem, "

        return prefix + base
