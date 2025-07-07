class Agent:
    """Ontological agent capable of state transitions and emotional exchange."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, shadows: dict | None = None) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.shadows: dict[str, float] = shadows or {}
        self.history = [state]
        self.connected_agents: list["Agent"] = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    # New methods for hidden influences and connections -------------------

    def calculate_shadow_influence(self) -> float:
        """Return cumulative emotional impact of hidden influences."""
        return sum(self.shadows.values())

    def update_emotion_from_shadows(self) -> None:
        """Modify emotion by applying shadow influences within bounds [0,1]."""
        self.emotion += self.calculate_shadow_influence()
        self.emotion = max(0.0, min(self.emotion, 1.0))

    def connect(self, other: "Agent") -> None:
        """Create a bidirectional emotional connection (krak)."""
        if other not in self.connected_agents:
            self.connected_agents.append(other)
            other.connected_agents.append(self)

    def share_emotion(self) -> None:
        """Share emotion with connected agents by averaging differences."""
        for agent in self.connected_agents:
            average = (self.emotion + agent.emotion) / 2
            self.emotion = average
            agent.emotion = average

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
        """Return a philosophical answer influenced by state and emotion."""
        base_response = ""
        if self.state == "Ego":
            base_response = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base_response = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base_response = "Vse resnice so eno, medsebojno povezane."

        if self.emotion > 0.5:
            return f"{base_response} Moja čustva so intenzivna ({self.emotion:.2f})."
        return base_response
