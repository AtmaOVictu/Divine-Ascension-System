class Agent:
    """Ontological agent with emotional and relational attributes."""

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
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.loyalty = loyalty
        self.relationships = relationships or {}
        self.decisions_history: list[str] = []
        self.team: list["Agent"] = []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def adjust_emotion(self, delta: float) -> None:
        """Adjust emotion gradually, influencing tension."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.tension += (delta / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def calculate_relationship_tension(self) -> float:
        """Return additional tension derived from relationship states."""
        return sum(abs(strength - 0.5) for strength in self.relationships.values()) / 10

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        if self.tension > 0.7 or self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        self.history.append(self.state)
        return self.state

    def make_moral_decision(self, situation: str) -> str:
        """Decide how to act in a moral dilemma based on current feelings."""
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
        """Simulate a collaborative task with the agent's team."""
        if not self.team:
            return f"{self.name} has no team to collaborate with."

        success_factor = 0.0
        for agent in self.team:
            success_factor += agent.loyalty
            if agent.emotional_state == "happy":
                success_factor += 1

        if success_factor > len(self.team):
            return f"{self.name}'s team successfully completes the task due to strong collaboration!"
        return f"{self.name}'s team fails the task due to lack of cohesion."

    def respond(self, question: str) -> str:
        """Return a philosophical answer depending on the current state."""
        if self.state == "Ego":
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {self.emotional_state})"
