"""Ontological agents and related utilities."""

from dataclasses import dataclass


@dataclass
class Emotion:
    """Represents an emotional state with a type and intensity."""

    kind: str = "neutral"
    intensity: float = 0.0


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: Emotion | None = None,
    ):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion or Emotion()
        self.history = [state]

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Update emotion type and intensity and adjust tension accordingly."""
        self.emotion = Emotion(kind, intensity)
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state and emotion."""
        prefix = ""
        if self.emotion.kind == "fear":
            prefix = "S tresočim glasom, "
        elif self.emotion.kind == "anger":
            prefix = "Z jezo, "
        elif self.emotion.kind == "joy":
            prefix = "Z veseljem, "

        if self.state == "Ego":
            msg = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            msg = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            msg = "Vse resnice so eno, medsebojno povezane."
        return prefix + msg
