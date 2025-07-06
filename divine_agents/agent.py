from typing import Optional

from .emotions import Emotion


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: Optional[Emotion] = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion: Emotion = emotion or Emotion("neutral", 0.0)
        self.history = [state]

    def update_emotion(self, name: str, value: float) -> None:
        """Update the current emotion and adjust tension accordingly."""
        self.emotion = Emotion(name, value)
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.level > 0.5:
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

        emotion_note = {
            "fear": " Čutim strah.",
            "joy": " Preveva me veselje.",
            "anger": " Občutim jezo."
        }.get(self.emotion.name, "")

        return base + emotion_note
