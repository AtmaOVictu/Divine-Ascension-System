"""Ontological agents capable of transitioning between philosophical states."""

from typing import List


class Agent:
    """Represents an agent with tension and emotion driven transitions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, emotion_type: str = "") -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotion_type = emotion_type
        self.history: List[str] = [state]

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set the current emotion and adjust tension accordingly."""

        self.emotion_type = emotion_type
        self.emotion = intensity

        if emotion_type in {"fear", "anger", "sorrow"}:
            self.tension = min(1.0, self.tension + intensity)
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - intensity / 2)
        else:
            self.tension = min(1.0, self.tension + intensity)

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
        self.tension = max(0.0, min(1.0, value))

    def transition(self) -> str:
        """Transition to a new state if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer reflecting the agent's state."""
        prefix = f"[{self.emotion_type}] " if self.emotion_type else ""

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
