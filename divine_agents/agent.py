from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(
        default_factory=lambda: {"fear": 0.0, "joy": 0.0, "anger": 0.0}
    )
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def set_emotion(self, name: str, value: float) -> None:
        """Set an emotion intensity and adjust tension accordingly."""
        if name not in self.emotions:
            raise ValueError(f"Unknown emotion '{name}'")
        self.emotions[name] = max(0.0, min(1.0, value))
        if name == "joy":
            self.tension = max(0.0, self.tension - value)
        else:
            self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _emotion_intensity(self) -> float:
        return max(self.emotions.values())

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self._emotion_intensity() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _base_response(self) -> str:
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on state and emotion."""
        base = self._base_response()
        emotion = max(self.emotions, key=self.emotions.get)
        intensity = self.emotions[emotion]
        if intensity == 0:
            return base
        prefix = {
            "fear": "[V strahu]",
            "anger": "[Z jezo]",
            "joy": "[Z veseljem]",
        }.get(emotion, "")
        return f"{prefix} {base}"
