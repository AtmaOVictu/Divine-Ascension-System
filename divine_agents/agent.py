from __future__ import annotations


class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, shadows: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.shadows: dict[str, float] = shadows if shadows else {}
        self.history = [state]
        self.connected_agents: list["Agent"] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def calculate_shadow_influence(self) -> float:
        """Return cumulative influence from hidden emotional factors."""
        return sum(self.shadows.values())

    def update_emotion_from_shadows(self) -> None:
        """Apply shadow influence to emotion with clamping."""
        self.emotion += self.calculate_shadow_influence()
        if self.emotion > 1.0:
            self.emotion = 1.0

    def connect(self, other: "Agent") -> None:
        """Form a two-way emotional connection with another agent."""
        if other not in self.connected_agents:
            self.connected_agents.append(other)
        if self not in other.connected_agents:
            other.connected_agents.append(self)

    def share_emotion(self) -> None:
        """Share emotional influence with connected agents."""
        for agent in self.connected_agents:
            agent.emotion += (self.emotion - agent.emotion) / 2

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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
        base_response = ""
        if self.state == "Ego":
            base_response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base_response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base_response = "Vse resnice so eno, medsebojno povezane."
        if self.emotion > 0.5:
            return f"{base_response} Moja custva so intenzivna."
        return base_response
