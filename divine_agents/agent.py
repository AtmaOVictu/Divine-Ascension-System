from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Agent:
    """Ontological agent capable of transitioning philosophical states."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotions: Dict[str, float] = field(default_factory=dict)
    history: List[str] = field(default_factory=list)

    STATES = ("Ego", "Jaz", "Enotnost")

    def __post_init__(self) -> None:
        self.history.append(self.state)

    def update_emotions(self, new_emotions: Dict[str, float]) -> None:
        """Update emotions and recompute tension."""
        self.emotions.update(new_emotions)
        if self.emotions:
            self.tension = sum(self.emotions.values()) / len(self.emotions)
        else:
            self.tension = 0.0

    def dominant_emotion(self) -> str:
        if not self.emotions:
            return "neutralno"
        emotion, value = max(self.emotions.items(), key=lambda x: x[1])
        return emotion if value > 0.5 else "mirno"

    def transition(self) -> str:
        """Transition state based on tension or dominant emotion."""
        max_emotion = max(self.emotions.values(), default=0.0)
        if self.tension > 0.7 or max_emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Provide answer reflecting current state and emotion."""
        mood = self.dominant_emotion()
        if self.state == "Ego":
            return f"({mood}) Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return f"({mood}) Resnica je relativna, oblikovana z našimi odnosi."
        return f"({mood}) Vse resnice so eno, medsebojno povezane."
