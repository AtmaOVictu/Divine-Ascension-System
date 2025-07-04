from __future__ import annotations

from typing import Dict


class Agent:
    """Ontological agent capable of emotional transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")
    THRESHOLD_TENSION = 0.7
    THRESHOLD_EMOTION = 0.5

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = 0.0
        self.emotions: Dict[str, float] = {}
        self.history = [state]

    def add_emotion(self, name: str, intensity: float) -> None:
        """Register an emotion and adjust tension."""
        self.emotions[name] = intensity
        if intensity > self.emotion:
            self.emotion = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > self.THRESHOLD_TENSION or self.emotion > self.THRESHOLD_EMOTION:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotions."""
        base = ""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > self.THRESHOLD_EMOTION and self.emotions:
            dominant = max(self.emotions, key=self.emotions.get)
            base += f" Čutim {dominant}."
        return base
