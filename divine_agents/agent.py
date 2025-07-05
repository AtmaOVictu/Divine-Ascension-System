"""Core agent logic for the Divine Ascension system."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Agent:
    """Ontological agent capable of changing philosophical states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    history: list[str] = field(default_factory=lambda: ["Ego"])

    def update_emotion(self, value: float) -> None:
        """Set emotion intensity and adjust tension accordingly."""
        self.emotion = max(-1.0, min(1.0, value))
        self.tension += self.emotion

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
        """Return a philosophical answer influenced by emotion and state."""
        emotion_prefix = ""
        if self.emotion > 0.5:
            emotion_prefix = "Navdihnjeno povem: "
        elif self.emotion < -0.5:
            emotion_prefix = "Z zaskrbljenostjo povem: "

        if self.state == "Ego":
            core = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            core = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            core = "Vse resnice so eno, medsebojno povezane."

        return f"{emotion_prefix}{core}"
