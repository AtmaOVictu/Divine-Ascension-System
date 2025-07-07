"""Core logic for ontological agents used in philosophical dialogues."""

from __future__ import annotations

from dataclasses import dataclass, field


TRANSITION_TENSION_THRESHOLD = 0.7
TRANSITION_EMOTION_THRESHOLD = 0.5


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str | None = None
    history: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, emotion_type: str, intensity: float) -> None:
        """Update the current emotion and modify tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        if emotion_type in {"fear", "anger"}:
            self.tension = min(1.0, self.tension + intensity)
        elif emotion_type == "joy":
            self.tension = max(0.0, self.tension - intensity)
        else:
            self.tension = min(1.0, self.tension + (intensity / 2))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > TRANSITION_TENSION_THRESHOLD or self.emotion > TRANSITION_EMOTION_THRESHOLD:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
