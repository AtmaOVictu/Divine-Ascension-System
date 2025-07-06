from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    emotion_type: Optional[str] = None
    history: List[str] = field(default_factory=lambda: ["Ego"])

    EMOTION_EFFECTS = {
        "fear": 1.0,
        "anger": 1.0,
        "joy": -0.5,
    }

    def set_emotion(self, emotion_type: str, intensity: float) -> None:
        """Set emotion type and intensity, adjusting tension accordingly."""
        self.emotion_type = emotion_type
        self.emotion = intensity
        effect = self.EMOTION_EFFECTS.get(emotion_type, 0)
        self.tension = max(0.0, self.tension + intensity * effect)

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
        """Return a philosophical answer depending on the current state and emotion."""
        base = {
            "Ego": "Resnica je absolutna in neodvisna od drugih.",
            "Jaz": "Resnica je relativna, oblikovana z našimi odnosi.",
            "Enotnost": "Vse resnice so eno, medsebojno povezane.",
        }[self.state]

        emotion_suffix = {
            "fear": "Skrbi me.",
            "anger": "To me jezi.",
            "joy": "To me veseli.",
            None: "",
        }[self.emotion_type]

        return f"{base} {emotion_suffix}".strip()
