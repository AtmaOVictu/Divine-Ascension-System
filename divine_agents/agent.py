"""Core agent logic handling states, emotions and responses."""

from __future__ import annotations

from dataclasses import dataclass, field


STATE_PRINCIPLES = {
    "Ego": "Resnica je absolutna in neodvisna od drugih.",
    "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
    "Enotnost": "Vse resnice so eno, medsebojno povezane.",
}


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # Emotions directly influence tension
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
        """Return a philosophical answer depending on the current state."""
        base = STATE_PRINCIPLES.get(self.state, "")
        if self.emotion > 0.7:
            tone = "z veliko strastjo"
        elif self.emotion > 0.4:
            tone = "mirno"
        else:
            tone = "brez čustev"
        return f"{tone}: {base}"
