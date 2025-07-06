from dataclasses import dataclass, field
from typing import List


@dataclass
class Agent:
    """Ontological agent capable of emotional transitions and philosophical responses."""

    name: str
    state: str = "Ego"
    tension: float = 0.0
    emotion: float = 0.0
    loyalty: float = 0.5
    experiences: List[str] = field(default_factory=list)

    def update_emotion(self, value: float) -> None:
        """Set emotion value and increase tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set the agent's tension."""
        self.tension = value

    def transition(self) -> str:
        """Move between ontological states if emotion or tension exceed thresholds."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.experiences.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return an answer that reflects the agent's ontological stance."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
