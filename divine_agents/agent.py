from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Ontological agent capable of transitioning states based on emotions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, kind: str, value: float) -> None:
        """Set an emotion intensity and update tension."""
        self.emotions[kind] = value
        # tension is the sum of all emotion intensities
        self.tension = sum(self.emotions.values())

    def update_tension(self, value: float) -> None:
        """Directly set the agent's tension."""
        self.tension = value

    def _emotion_threshold(self) -> float:
        return max(self.emotions.values(), default=0.0)

    def transition(self) -> str:
        """Perform a state transition if thresholds are met."""
        if self.tension > 0.7 or self._emotion_threshold() > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def _emotion_prefix(self) -> str:
        if not self.emotions:
            return ""
        emotion, intensity = max(self.emotions.items(), key=lambda x: x[1])
        if intensity <= 0.2:
            return ""
        return f"[{emotion.capitalize()} {intensity:.2f}] "

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        prefix = self._emotion_prefix()
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return prefix + base
