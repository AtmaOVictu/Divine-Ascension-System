from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Agent:
    """Ontological agent capable of emotional reactions and state transitions."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotion(self, kind: str, intensity: float) -> None:
        """Set a named emotion and adjust tension accordingly."""
        self.emotions[kind] = intensity
        if kind in {"fear", "anger"}:
            self.tension = min(1.0, self.tension + intensity)
        elif kind == "joy":
            # Joy relaxes the agent and lowers tension
            self.tension = max(0.0, self.tension - intensity)
        else:
            self.tension += intensity

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def _dominant_emotion(self) -> Optional[str]:
        return max(self.emotions, key=self.emotions.get) if self.emotions else None

    def transition(self) -> str:
        """Perform state transition if emotional or tension thresholds are exceeded."""
        emotion_trigger = any(value > 0.5 for value in self.emotions.values())
        if self.tension > 0.7 or emotion_trigger:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer influenced by the current state and emotion."""
        prefix = ""
        dominant = self._dominant_emotion()
        if dominant:
            prefix = f"({dominant}) "

        if self.state == "Ego":
            return prefix + "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return prefix + "Resnica je relativna, oblikovana z našimi odnosi."
        return prefix + "Vse resnice so eno, medsebojno povezane."
