"""Core agent functionality for ontological state transitions and dialogue."""

from dataclasses import dataclass, field
from typing import ClassVar, Dict


@dataclass
class Agent:
    """Represent an ontological agent capable of transitioning states."""

    # available ontological phases
    STATES: ClassVar[tuple[str, ...]] = ("Ego", "Jaz", "Enotnost")

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: str = "neutral"
    history: list[str] = field(default_factory=list)

    # how emotions influence tension
    EMOTION_EFFECTS: ClassVar[Dict[str, float]] = {
        "fear": 0.5,
        "joy": 0.3,
        "anger": 0.7,
        "neutral": 0.0,
    }

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, label: str | None = None) -> None:
        """Update emotion intensity and adjust tension with a labelled emotion."""

        self.emotion = value
        if label:
            self.emotion_label = label
        effect = value * self.EMOTION_EFFECTS.get(self.emotion_label, 0)
        self.tension += effect

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

    def respond(self, question: str = "") -> str:
        """Return a philosophical answer influenced by emotion and state."""

        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        prefix_map = {
            "fear": "S strahom",
            "joy": "Z veseljem",
            "anger": "Z jezo",
            "neutral": "",
        }

        if self.emotion > 0.5:
            prefix = prefix_map.get(self.emotion_label, "").strip()
            if prefix:
                return f"{prefix} menim, da {base.lower()}"
        return base
