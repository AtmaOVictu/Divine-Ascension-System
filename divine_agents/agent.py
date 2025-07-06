class Agent:
    """Represent an ontological agent with emotional and moral context."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        loyalty: float = 0.5,
    ) -> None:
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.loyalty = loyalty

        self.history = [state]
        self.trust: dict[str, float] = {}

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def update_relationship(self, other: "Agent", delta: float) -> None:
        """Adjust trust level toward another agent."""
        current = self.trust.get(other.name, 0.5)
        self.trust[other.name] = min(1.0, max(0.0, current + delta))

    def transition(self) -> str:
        """Perform state transition if thresholds or experiences warrant it."""
        threshold = self.tension > 0.7 or self.emotion > 0.5
        repeated = self.history.count(self.state) > 2
        if threshold or repeated:
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
        """Determine a moral action based on emotion, tension and loyalty."""
        if self.tension > 0.8 or self.emotion < -0.5:
            decision = f"{self.name} prioritizes self-preservation in {situation}."
        elif self.loyalty > 0.7 and self.emotion > 0.3:
            decision = f"{self.name} helps others selflessly in {situation}."
        else:
            decision = f"{self.name} decides to act in their own interest in {situation}."
        self.history.append(decision)
        return decision

    def team_decision(self, team: list["Agent"]) -> str:
        """Make a team decision based on trust towards teammates."""
        if not team:
            return f"{self.name} has no team to consult."
        trust_levels = [self.trust.get(member.name, 0.5) for member in team]
        avg_trust = sum(trust_levels) / len(trust_levels)
        if avg_trust > 0.6:
            return f"{self.name}'s team takes a risk with optimism!"
        if avg_trust < 0.4:
            return f"{self.name}'s team avoids risk due to lack of trust."
        return f"{self.name}'s team makes a cautious decision."
