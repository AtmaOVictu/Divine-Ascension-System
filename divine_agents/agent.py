"""Ontological agent model with emotional-driven state transitions."""

from typing import Dict


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotions: Dict[str, float] | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotions: Dict[str, float] = emotions or {
            "fear": 0.0,
            "joy": 0.0,
            "anger": 0.0,
        }
        self.history = [state]

    @property
    def emotion_level(self) -> float:
        """Return highest emotion intensity."""
        return max(self.emotions.values(), default=0.0)

    def update_emotion(self, emotion: str, intensity: float) -> None:
        """Update a specific emotion and adjust tension."""
        if emotion not in self.emotions:
            self.emotions[emotion] = 0.0
        self.emotions[emotion] = intensity
        if intensity > self.tension:
            self.tension = intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion_level > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer based on current state and emotions."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_level > 0.5:
            if self.emotions.get("anger", 0) > 0.5:
                return f"{base} Čutim jezo."
            if self.emotions.get("fear", 0) > 0.5:
                return f"{base} Občutim strah."
            if self.emotions.get("joy", 0) > 0.5:
                return f"{base} Preplavlja me veselje."
        return base
