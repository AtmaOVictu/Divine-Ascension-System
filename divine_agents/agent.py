from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, emotion: str, value: float) -> None:
        """Set an emotion intensity and adjust tension."""
        self.emotions[emotion] = value
        self.tension += value

    def set_tension(self, value: float) -> None:
        """Directly set the agent's tension level."""
        self.tension = value

    def _emotion_threshold(self) -> bool:
        return any(level > 0.5 for level in self.emotions.values())

    def transition(self) -> str:
        """Transition to the next state if thresholds are met."""
        if self.tension > 0.7 or self._emotion_threshold():
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def philosophical_principle(self) -> str:
        """Return the principle for the current ontological state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def respond(self, question: str) -> str:
        """Return a philosophical response influenced by emotions."""
        base = self.philosophical_principle()
        if self.emotions:
            strongest = max(self.emotions, key=self.emotions.get)
            intensity = self.emotions[strongest]
            if intensity > 0.5:
                return f"{base} Moje {strongest} je izrazito."
        return base
