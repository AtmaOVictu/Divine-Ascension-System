"""Module defining ontological agents capable of state transitions."""

from typing import Dict


class Agent:
    """Represents an ontological agent with emotions and tension."""

    STATES = ("Ego", "Jaz", "Enotnost")
    EMOTION_MAP: Dict[str, float] = {
        "fear": 0.6,
        "anger": 0.7,
        "joy": 0.4,
        "sorrow": 0.5,
        "neutral": 0.0,
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def feel(self, name: str) -> None:
        """Set emotion based on a named feeling.

        Parameters
        ----------
        name:
            The name of the emotion (e.g., "fear", "joy"). If the name is
            unknown, ``neutral`` is assumed.
        """
        self.update_emotion(self.EMOTION_MAP.get(name, 0.0))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
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

        if self.emotion > 0.6:
            prefix = "Strastno"
        elif self.emotion > 0.3:
            prefix = "Umirjeno"
        else:
            prefix = "Mirno"

        return f"{prefix}: {base}"
