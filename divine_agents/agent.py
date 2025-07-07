class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, shadows: dict | None = None):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.shadows = shadows if shadows else {}
        self.history = [state]
        self.connected_agents: list["Agent"] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    # --- Shadow and Connection Mechanics ---
    def calculate_shadow_influence(self) -> float:
        """Aggregate hidden emotional influences."""
        return sum(self.shadows.values())

    def update_emotion_from_shadows(self) -> None:
        """Modify emotion based on shadow influence."""
        self.emotion += self.calculate_shadow_influence()
        if self.emotion > 1.0:
            self.emotion = 1.0

    def connect(self, other: "Agent") -> None:
        """Establish a two-way emotional connection with another agent."""
        if other not in self.connected_agents:
            self.connected_agents.append(other)
            other.connected_agents.append(self)

    def share_emotion(self) -> None:
        """Share emotional state with connected agents."""
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
