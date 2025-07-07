"""Core classes representing agents used in philosophical dialogues."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Agent:
    """Ontological agent capable of transitioning between states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Initialize history with the starting state."""
        self.history.append(self.state)

    def update_emotion(self, value: float, emotion_type: str | None = None) -> None:
        """Update emotion intensity and optionally set emotion type.

        The agent's tension increases with the intensity of the emotion.
        """

        self.emotion = value
        if emotion_type is not None:
            self.emotion_type = emotion_type
        self.tension += value

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
        """Return a philosophical answer depending on current and emotional state."""

        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion_type == "fear":
            base += " Občutim strah ob tej misli."
        elif self.emotion_type == "joy":
            base += " Preveva me veselje."
        elif self.emotion_type == "anger":
            base += " Čutim jezo v sebi."

        return base
