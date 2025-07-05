from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: List[str] = field(default_factory=lambda: ["Ego"])

    #: Influence of emotions on tension level.
    EMOTION_EFFECT = {"fear": 0.4, "anger": 0.5, "joy": -0.3}

    def set_emotion(self, name: str, intensity: float) -> None:
        """Assign an emotion with intensity and adjust tension."""
        self.emotion_name = name
        self.emotion = intensity
        self.tension += intensity * self.EMOTION_EFFECT.get(name, 0.0)

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
        """Return a philosophical answer depending on state and emotion."""
        prefix = {
            "anger": "Z jezo odgovarjam:",
            "fear": "S strahom odvrnem:",
            "joy": "Z veseljem delim:",
        }.get(self.emotion_name, "Odgovarjam:")

        if self.state == "Ego":
            truth = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            truth = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            truth = "Vse resnice so eno, medsebojno povezane."

        return f"{prefix} {truth}"
