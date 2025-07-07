from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_label: Optional[str] = None
    history: List[str] = field(default_factory=list)

    PHILOSOPHY = {
        "Ego": "Resnica je absolutna in neodvisna od drugih.",
        "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
        "Enotnost": "Vse resnice so eno, medsebojno povezane.",
    }

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, value: float, label: Optional[str] = None) -> None:
        """Update emotion intensity, optionally setting its label and adjust tension."""
        self.emotion = value
        if label:
            self.emotion_label = label
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the tension level."""
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
        """Return a philosophical answer influenced by ontological state and emotion."""
        base = self.PHILOSOPHY.get(self.state, "")
        mood = ""
        if self.emotion_label == "anger":
            mood = "Z jezo odgovarjam, da "
        elif self.emotion_label == "fear":
            mood = "V strahu povem, da "
        elif self.emotion_label == "joy":
            mood = "Z veseljem povem, da "
        return f"{mood}{base}"
