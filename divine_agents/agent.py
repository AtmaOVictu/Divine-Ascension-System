from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Agent:
    """Ontological agent capable of emotional state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=lambda: ["Ego"])

    STATES = ("Ego", "Jaz", "Enotnost")

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Update a specific emotion and adjust tension."""
        self.emotions[kind] = intensity
        self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def dominant_emotion(self) -> Optional[str]:
        """Return the dominant emotion if any."""
        if not self.emotions:
            return None
        return max(self.emotions, key=self.emotions.get)

    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or any(v > 0.5 for v in self.emotions.values()):
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state."""
        note = ""
        dominant = self.dominant_emotion()
        if dominant:
            note = f" (občuti {dominant})"

        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih." + note
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi." + note
        return "Vse resnice so eno, medsebojno povezane." + note
