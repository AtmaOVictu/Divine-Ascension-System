from __future__ import annotations

"""Ontological agent implementation."""

from dataclasses import dataclass, field
from typing import List

from .enums import Emotion, State


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: State = State.EGO
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Emotion = Emotion.NEUTRAL
    history: List[State] = field(default_factory=lambda: [State.EGO])

    def update_emotion(self, emotion_type: Emotion, intensity: float) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        if intensity > 0.5:
            self.tension += 0.1
        if emotion_type in {Emotion.FEAR, Emotion.ANGER}:
            self.tension += 0.1
        elif emotion_type is Emotion.JOY:
            self.tension = max(0.0, self.tension - 0.05)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> State:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state is State.EGO:
                self.state = State.JAZ
            elif self.state is State.JAZ:
                self.state = State.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state is State.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state is State.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
