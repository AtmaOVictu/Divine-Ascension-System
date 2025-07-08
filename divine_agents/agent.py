from enum import Enum
from dataclasses import dataclass, field


class Emotion(Enum):
    """Enumerates basic emotions that influence agent tension."""

    FEAR = "fear"
    JOY = "joy"
    ANGER = "anger"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion_level: float = 0.0
    emotion_type: Emotion | None = None
    history: list[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, emotion: Emotion, intensity: float) -> None:
        """Update emotion and adjust tension accordingly.

        Negative emotions (fear, anger) increase tension, while joy reduces it.
        Intensity is clamped between 0 and 1.
        """
        intensity = min(1.0, max(0.0, intensity))
        self.emotion_type = emotion
        self.emotion_level = intensity

        if emotion in {Emotion.FEAR, Emotion.ANGER}:
            self.tension = min(1.0, self.tension + intensity)
        else:
            self.tension = max(0.0, self.tension - intensity)

    def update_tension(self, value: float) -> None:
        """Directly set tension level (clamped between 0 and 1)."""
        self.tension = min(1.0, max(0.0, value))

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
        """Return a philosophical answer depending on the current state."""
        prefix = ""
        if self.emotion_type == Emotion.FEAR:
            prefix = "(prestrašen) "
        elif self.emotion_type == Emotion.ANGER:
            prefix = "(jezen) "
        elif self.emotion_type == Emotion.JOY:
            prefix = "(vesel) "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
