class Agent:
    """Ontological agent capable of transitioning states and making decisions."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotional_state: str = "neutral",
        loyalty: float = 0.5,
        team: list | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.loyalty = loyalty
        self.team = team or []
        self.relationships: dict[str, float] = {}
        self.decisions_history: list[str] = []
        self.history = [state]

    # ------------------------------------------------------------------
    # Updating emotion and tension
    # ------------------------------------------------------------------
    def update_emotion(self, value: float, emotional_state: str | None = None) -> None:
        """Update numeric emotion intensity and optionally set emotional state."""
        self.emotion = value
        if emotional_state:
            self.emotional_state = emotional_state
        # emotion contributes to tension
        self.tension = max(0.0, min(1.0, self.tension + value))

    def calculate_relationship_tension(self) -> float:
        """Return additional tension derived from relationship imbalances."""
        if not self.relationships:
            return 0.0
        return sum(abs(score - 0.5) for score in self.relationships.values()) / 10.0

    def update_tension(self) -> None:
        """Slowly increase tension from emotion and relationships."""
        self.tension += (self.emotion / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    # ------------------------------------------------------------------
    # State management and responses
    # ------------------------------------------------------------------
    def transition(self) -> str:
        """Perform state transition when thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def respond(self, question: str) -> str:
        """Return a philosophical answer according to the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    # ------------------------------------------------------------------
    # Decision logic
    # ------------------------------------------------------------------
    def make_moral_decision(self, situation: str) -> str:
        """Decide how to act in a moral dilemma based on emotion and loyalty."""
        if self.emotional_state == "fearful":
            if self.loyalty > 0.7:
                decision = f"{self.name} chooses to help others despite fear due to loyalty."
            else:
                decision = f"{self.name} decides to act selfishly, avoiding risk."
        elif self.emotional_state == "happy":
            if self.loyalty > 0.7:
                decision = f"{self.name} helps others selflessly in {situation}."
            else:
                decision = f"{self.name} focuses on personal gain, despite team needs."
        else:
            decision = f"{self.name} hesitates, torn between loyalty and personal interest."
        self.decisions_history.append(decision)
        return decision

    def collaborative_task(self) -> str:
        """Simulate a collaborative task involving the agent's team."""
        success_factor = 0
        for agent in self.team:
            success_factor += agent.loyalty + (1 if agent.emotional_state == "happy" else 0)
        if self.team and success_factor > len(self.team):
            return f"{self.name}'s team successfully completes the task due to strong collaboration!"
        return f"{self.name}'s team fails the task due to lack of cohesion."
