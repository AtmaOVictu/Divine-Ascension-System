from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple


class State(Enum):
    """Enumeration of ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Emotions:
    """Container for emotional values."""

    fear: float = 0.0
    joy: float = 0.0
    anger: float = 0.0

    def intensity(self) -> float:
        """Return average absolute intensity of emotions."""
        values = [self.fear, self.joy, self.anger]
        return sum(abs(v) for v in values) / len(values)


class Agent:
    """Represents an ontological agent with memory and emotional learning."""

    STATES = (State.EGO.value, State.JAZ.value, State.ENOTNOST.value)
    TRANSITION_TENSION = 0.7
    EMOTION_THRESHOLD = 0.5

    def __init__(self, name: str, state: State | str = State.EGO, tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = State(state) if isinstance(state, str) else state
        self.tension = tension
        self.emotion = emotion
        self.emotions = Emotions()
        self.history: List[Tuple[State, float]] = [(self.state, self.tension)]

    # ------------------------------------------------------------------
    # Emotion and tension handling
    # ------------------------------------------------------------------
    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, **kwargs: float) -> None:
        """Update specific emotions and recompute tension."""
        for emotion, value in kwargs.items():
            if hasattr(self.emotions, emotion):
                setattr(self.emotions, emotion, value)
        self.tension += self.emotions.intensity()
        self.transition()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # ------------------------------------------------------------------
    # Learning and clustering
    # ------------------------------------------------------------------
    def learn_from_history(self) -> None:
        """Adjust tension threshold based on historical average."""
        avg_tension = sum(t for _, t in self.history) / len(self.history)
        self.TRANSITION_TENSION = max(0.5, min(1.0, avg_tension))

    def get_cluster(self) -> str:
        """Classify agent into a simple tension-based cluster."""
        avg_tension = sum(t for _, t in self.history) / len(self.history)
        if avg_tension < 0.5:
            return "low"
        if avg_tension < 1.0:
            return "medium"
        return "high"

    # ------------------------------------------------------------------
    # State handling and responses
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        triggered = self.tension > self.TRANSITION_TENSION or self.emotion > self.EMOTION_THRESHOLD or self.emotions.intensity() > self.EMOTION_THRESHOLD
        if triggered:
            if self.state == State.EGO:
                self.state = State.JAZ
            elif self.state == State.JAZ:
                self.state = State.ENOTNOST
        self.history.append((self.state, self.tension))
        return self.state.value

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and mood."""
        mood = self._describe_mood()
        if self.state == State.EGO:
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == State.JAZ:
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} {mood}".strip()

    def _describe_mood(self) -> str:
        """Return a textual description of the strongest emotion."""
        intensities = {
            'strah': self.emotions.fear,
            'veselje': self.emotions.joy,
            'jeza': self.emotions.anger,
        }
        if not any(intensities.values()):
            return ""
        strongest = max(intensities, key=lambda k: abs(intensities[k]))
        return f"Občutim {strongest}."
