class Agent:
    """Represent an ontological agent with emotions and loyalty."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, loyalty: float = 0.5):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty
        self.relationships = {}
        self.decisions_history = []
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion and adjust tension with a slower growth."""
        self.emotion = value
        self.update_tension(self.tension + (value / 10) * 0.9)

    def update_tension(self, value: float) -> None:
        """Set tension level with clamping between 0 and 1."""
        self.tension = max(0.0, min(1.0, value))

    def calculate_relationship_tension(self) -> float:
        """Return additional tension derived from negative relationships."""
        negative = [v for v in self.relationships.values() if v < 0]
        return abs(sum(negative)) / 10

    def interact_with(self, other: "Agent", effect: float) -> None:
        """Adjust relationship with another agent and update emotion."""
        self.relationships.setdefault(other.name, 0.0)
        self.relationships[other.name] += effect
        self.update_emotion(min(1.0, self.emotion + effect))

    def transition(self) -> str:
        """Perform state transition if thresholds are exceeded."""
        # account for additional tension from relationships
        self.update_tension(self.tension + self.calculate_relationship_tension())

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
        """Make a moral decision based on emotion and loyalty."""
        if self.emotion > 0.5 and self.loyalty > 0.7:
            decision = f"{self.name} chooses to help others in {situation}."
        elif self.emotion > 0.5:
            decision = f"{self.name} avoids risk in {situation}."
        else:
            decision = f"{self.name} hesitates in {situation}."
        self.decisions_history.append(decision)
        return decision

    def collaborative_task(self, team: list) -> str:
        """Simulate a team task and return the outcome."""
        success_factor = 0
        for agent in team:
            mood_bonus = 1 if agent.emotion > 0.5 else 0
            success_factor += agent.loyalty + mood_bonus

        if success_factor > len(team):
            return f"{self.name}'s team succeeds through unity."
        return f"{self.name}'s team fails due to low cohesion."
