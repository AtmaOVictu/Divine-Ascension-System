from __future__ import annotations

from .emotion import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: Emotion | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Emotion | None = emotion
        self.history = [state]

    def update_emotion(self, emotion: Emotion) -> None:
        """Update emotion and adjust tension accordingly."""
        self.emotion = emotion
        self.tension += emotion.intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        emotion_intensity = self.emotion.intensity if self.emotion else 0.0
        if self.tension > 0.7 or emotion_intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion:
            if self.emotion.kind in {"fear", "anger"}:
                base += f" Čutim {self.emotion.kind}."
            elif self.emotion.kind == "joy":
                base += " Občutim veselje." 
            else:
                base += f" Čustvo: {self.emotion.kind}."
        return base
