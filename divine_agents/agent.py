from dataclasses import dataclass, field
from enum import Enum


class OntologicalState(str, Enum):
    """Possible ontological states for an agent."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: OntologicalState = OntologicalState.EGO
    tension: float = 0.0
    emotion: float = 0.0
    emotion_name: str = "neutral"
    history: list[str] = field(default_factory=lambda: [OntologicalState.EGO])

    def update_emotion(self, value: float, name: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if name:
            self.emotion_name = name
        # emotions like fear or anger increase tension
        if self.emotion_name in {"fear", "anger"}:
            self.tension += value
        elif self.emotion_name == "joy":
            self.tension = max(0.0, self.tension - value / 2)
        else:
            self.tension += value / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> OntologicalState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == OntologicalState.EGO:
                self.state = OntologicalState.JAZ
            elif self.state == OntologicalState.JAZ:
                self.state = OntologicalState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == OntologicalState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == OntologicalState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
