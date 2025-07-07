from __future__ import annotations

from typing import Dict, List


class Agent:
    """Ontological agent capable of state transitions and emotional influence."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        shadows: Dict[str, float] | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.shadows: Dict[str, float] = shadows or {}
        self.history: List[str] = [state]
        self.connected_agents: List[Agent] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # New functionality -----------------------------------------------------

    def calculate_shadow_influence(self) -> float:
        """Return the summed hidden emotional influences (shadows)."""
        return sum(self.shadows.values())

    def update_emotion_from_shadows(self) -> None:
        """Apply shadow influences to the current emotion value."""
        self.emotion += self.calculate_shadow_influence()
        if self.emotion > 1.0:
            self.emotion = 1.0

    def connect(self, other: "Agent") -> None:
        """Establish a two-way emotional connection with another agent."""
        if other not in self.connected_agents:
            self.connected_agents.append(other)
        if self not in other.connected_agents:
            other.connected_agents.append(self)

    def share_emotion(self) -> None:
        """Share emotions with all connected agents by averaging values."""
        for agent in self.connected_agents:
            agent.emotion += (self.emotion - agent.emotion) / 2

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        self.update_emotion_from_shadows()
        self.share_emotion()
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base} Moja čustva so intenzivna."
        return base
