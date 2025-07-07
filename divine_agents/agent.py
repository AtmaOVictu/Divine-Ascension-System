from enum import Enum


class AgentState(Enum):
    """Enumeration of agent ontological states."""

    EGO = "Ego"
    JAZ = "Jaz"
    ENOTNOST = "Enotnost"


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    def __init__(self, name: str, state: AgentState = AgentState.EGO, tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
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
