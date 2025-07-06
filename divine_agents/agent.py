class Agent:
    """Represents an ontological agent capable of transitioning states."""

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
        self.relationship_strength: dict[str, float] = relationships or {}
        self.decisions_history: list[str] = []
        self.team: list["Agent"] = []
        self.history = [state]

    def update_emotion(self, value: float, state: str | None = None) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        if state is not None:
            self.emotional_state = state
        self.tension += (value / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0.0, min(1.0, self.tension))

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def calculate_relationship_tension(self) -> float:
        """Calculate additional tension based on relationships."""
        if not self.relationship_strength:
            return 0.0
        return sum(self.relationship_strength.values()) * 0.05

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
            base = "Resnica je absolutna in neodvisna od drugih."
        elif self.state == "Jaz":
            base = "Resnica je relativna, oblikovana z našimi odnosi."
        else:
            base = "Vse resnice so eno, medsebojno povezane."
        return f"{base} (Čustvo: {self.emotional_state})"

    # ----- Moral and collaborative behaviour -----

    def make_moral_decision(self, situation: str) -> str:
        """Make a moral decision influenced by emotion and loyalty."""
        if self.emotional_state == "fearful":
            if self.loyalty > 0.7:
                decision = f"{self.name} chooses to help others despite fear due to loyalty."
            else:
                decision = f"{self.name} acts selfishly, avoiding risk."
        elif self.emotional_state == "happy":
            if self.loyalty > 0.7:
                decision = f"{self.name} selflessly helps others in {situation}."
            else:
                decision = f"{self.name} focuses on personal gain, despite team needs."
        else:
            decision = f"{self.name} hesitates, torn between loyalty and personal interest."
        self.decisions_history.append(decision)
        return decision

    def team_decision(self) -> str:
        """Decide on a course of action based on team emotions and loyalty."""
        if not self.team:
            return f"{self.name} has no team to consult."
        team_loyalty = sum(agent.loyalty for agent in self.team)
        happy_agents = sum(1 for agent in self.team if agent.emotional_state == "happy")
        if team_loyalty > len(self.team) / 2 and happy_agents > len(self.team) / 2:
            return f"{self.name}'s team decides to take a risk with optimism and loyalty!"
        return f"{self.name}'s team avoids risk due to conflict or fear."

    def show_empathy(self, other_agent: "Agent") -> str:
        """Provide an empathetic response depending on relationship strength."""
        strength = self.relationship_strength.get(other_agent.name, 0)
        if other_agent.emotional_state == "fearful" and strength > 0.7:
            return f"{self.name} comforts {other_agent.name}, offering reassurance."
        if other_agent.emotional_state == "sad" and strength > 0.7:
            return f"{self.name} uplifts {other_agent.name}, offering encouragement."
        if other_agent.emotional_state == "happy" and strength > 0.7:
            return f"{self.name} shares in {other_agent.name}'s joy enthusiastically."
        return f"{self.name} observes {other_agent.name}'s emotion but does not act."
