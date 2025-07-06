class Agent:
    """Represent an ontological agent with emotions and loyalty."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotional_state: str = "neutral",
        loyalty: float = 0.5,
        relationships: dict | None = None,
        team: list | None = None,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.loyalty = loyalty
        self.relationships = relationships or {}
        self.team = team or []
        self.history = [state]
        self.decisions_history = []

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = max(0, min(1, value))
        self.tension += self.emotion
        self.compute_tension()

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0, min(1, value))

    def calculate_relationship_tension(self) -> float:
        """Return additional tension derived from negative relationships."""
        tension = 0.0
        for strength in self.relationships.values():
            if strength < 0:
                tension += -strength
        return tension

    def compute_tension(self) -> None:
        """Update tension considering emotion and relationships."""
        self.tension += (self.emotion / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0, min(1, self.tension))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def interact_with(self, other: "Agent") -> None:
        """Influence emotions through interaction with another agent."""
        influence = other.emotion * 0.5
        self.update_emotion(min(1, self.emotion + influence))
        other.update_emotion(min(1, other.emotion + influence))

    def make_moral_decision(self, situation: str) -> str:
        """Return a moral decision statement based on emotion and loyalty."""
        if self.emotional_state == "fearful":
            if self.loyalty > 0.7:
                decision = (
                    f"{self.name} chooses to help others despite fear due to loyalty."
                )
            else:
                decision = f"{self.name} acts selfishly, avoiding risk."
        elif self.emotional_state == "happy":
            if self.loyalty > 0.7:
                decision = f"{self.name} helps others selflessly in {situation}."
            else:
                decision = (
                    f"{self.name} focuses on personal gain, despite team needs."
                )
        else:
            decision = f"{self.name} hesitates, torn between loyalty and personal interest."
        self.decisions_history.append(decision)
        return decision

    def collaborative_task(self) -> str:
        """Evaluate team collaboration based on loyalty and emotions."""
        success_factor = 0.0
        for agent in self.team:
            bonus = 1 if agent.emotional_state == "happy" else 0
            success_factor += agent.loyalty + bonus
        if self.team and success_factor > len(self.team):
            return (
                f"{self.name}'s team successfully completes the task due to "
                "strong collaboration!"
            )
        return f"{self.name}'s team fails the task due to lack of cohesion."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
