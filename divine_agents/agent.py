from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: str = "neutral"
    history: List[str] = field(default_factory=list, init=False)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, kind: str = "neutral") -> None:
        """Update emotion and modify tension according to emotion type."""
        self.emotion = value
        self.emotion_type = kind

        if kind in {"fear", "anger"}:
            self.tension = min(1.0, self.tension + value)
        elif kind == "joy":
            self.tension = max(0.0, self.tension - value)

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
        """Return a philosophical answer influenced by emotional state."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z nasimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        prefix = {
            "fear": "V strahu povem:",
            "anger": "Z jezo izjavljam:",
            "joy": "Z veseljem povem:",
        }.get(self.emotion_type, "")

        return f"{prefix} {base}".strip()
