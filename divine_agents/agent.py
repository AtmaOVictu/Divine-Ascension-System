from __future__ import annotations

from dataclasses import dataclass, field

from .emotion import Emotion


@dataclass
class Agent:
    """Ontological agent capable of state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: Emotion = field(default_factory=Emotion)
    history: list[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, intensity: float, **kwargs) -> None:
        """Update emotion intensity and adjust tension."""
        self.emotion.intensity = intensity
        self.tension += intensity
        # allow updating other emotion components
        for key, value in kwargs.items():
            if hasattr(self.emotion, key):
                setattr(self.emotion, key, value)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> str:
        """Transition between states when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion.intensity > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by emotional intensity."""
        prefix = "Močno čutim, da " if self.emotion.intensity > 0.5 else "Menim, da "
        if self.state == "Ego":
            return prefix + "resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "vse resnice so eno, medsebojno povezane."
