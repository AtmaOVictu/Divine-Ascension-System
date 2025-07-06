class Agent:
    """Represents an ontological agent with emotions and loyalty."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        emotional_state: str = "neutral",
        loyalty: float = 0.5,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.loyalty = loyalty
        self.relationships = {}
        self.decisions_history = []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        # more gradual tension growth influenced by emotions
        self.tension += (value / 10) * 0.9
        self.tension = max(0.0, min(1.0, self.tension))

    def adjust_emotion(self, delta: float, state: str) -> None:
        """Adjust emotion and emotional_state based on feedback."""
        self.emotion = max(0.0, min(1.0, self.emotion + delta))
        self.emotional_state = state
        self.update_tension(self.tension + delta)

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = max(0.0, min(1.0, value))

    def calculate_relationship_tension(self) -> float:
        """Return additional tension generated from relationships."""
        if not self.relationships:
            return 0.0
        return sum(abs(val - 0.5) for val in self.relationships.values()) / (
            len(self.relationships) * 10
        )

    def update_tension_dynamic(self) -> None:
        """Update tension considering emotions and relationships."""
        self.tension += (self.emotion / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
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
            return "Resnica je absolutna in neodvisna od drugih."
        if self.state == "Jaz":
            return "Resnica je relativna, oblikovana z našimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."

    def make_moral_decision(self, situation: str) -> str:
        """Make a moral decision influenced by emotion and loyalty."""
        if self.emotional_state == "fearful":
            if self.loyalty > 0.7:
                decision = (
                    f"{self.name} chooses to help others despite fear due to loyalty."
                )
            else:
                decision = f"{self.name} decides to act selfishly, avoiding risk."
        elif self.emotional_state == "happy":
            if self.loyalty > 0.7:
                decision = f"{self.name} helps others selflessly in {situation}."
            else:
                decision = (
                    f"{self.name} focuses on personal gain, despite team needs."
                )
        else:
            decision = (
                f"{self.name} hesitates, torn between loyalty and personal interest."
            )

        self.decisions_history.append(decision)
        return decision

    def team_decision(self, team: list, situation: str) -> str:
        """Make a group decision based on team emotions and loyalty."""
        factor = sum(a.loyalty + (1 if a.emotional_state == "happy" else 0) for a in team)
        if factor > len(team):
            return f"{self.name}'s team agrees to help in {situation}."
        return f"{self.name}'s team avoids the task in {situation}."

    def collaborative_task(self, team: list) -> str:
        """Simulate a collaborative task where success depends on team cohesion."""
        success = 0
        for agent in team:
            success += agent.loyalty + (1 if agent.emotional_state == "happy" else 0)
        if success > len(team):
            return f"{self.name}'s team successfully completes the task due to strong collaboration!"
        return f"{self.name}'s team fails the task due to lack of cohesion."
