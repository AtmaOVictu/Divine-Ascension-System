"""Core objects representing philosophical agents."""

from dataclasses import dataclass, field
from .state import AgentState


@dataclass
class Agent:
    """Represents an ontological agent capable of transitioning states."""

    name: str
    state: AgentState = AgentState.EGO
    tension: float = 0.0
    emotion: float = 0.0
    history: list = field(default_factory=lambda: [AgentState.EGO])

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # emotion contributes to overall tension
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def transition(self) -> AgentState:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == AgentState.EGO:
                self.state = AgentState.JAZ
            elif self.state == AgentState.JAZ:
                self.state = AgentState.ENOTNOST
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == AgentState.EGO:
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == AgentState.JAZ:
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
