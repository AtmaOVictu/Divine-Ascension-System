"""Ontological agent representation."""

from dataclasses import dataclass, field
from .emotion import Emotion


@dataclass
class Agent:
    """Agent that transitions through ontological states based on emotions and tension."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: Emotion = Emotion.NEUTRAL
    history: list[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, emotion: Emotion) -> None:
        """Set an emotional state and adjust tension accordingly."""
        self.emotion = emotion
        self.tension += emotion.value

    @property
    def emotion_level(self) -> float:
        """Return the numeric intensity of the current emotion."""
        return self.emotion.value

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
        """Return a philosophical answer depending on the current state and emotion."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion != Emotion.NEUTRAL:
            base += f" Čutim {self.emotion.name.lower()}."
        return base
