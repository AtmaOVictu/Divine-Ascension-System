class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 emotional_state: str = "neutral"):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.emotional_state = emotional_state
        self.history = [state]
        self.team = []
        self.decisions_history: list[str] = []

    def update_emotion(self, value: float, state: str | None = None) -> None:
        """Update emotion intensity, optionally setting emotional state."""
        self.emotion = value
        if state is not None:
            self.emotional_state = state
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

    def add_teammate(self, agent: "Agent") -> None:
        """Add another agent to this agent's team."""
        if agent not in self.team and agent is not self:
            self.team.append(agent)

    def calculate_relationship_tension(self) -> float:
        """Return additional tension based on teammates' emotions."""
        return sum(mate.emotion * 0.1 for mate in self.team)

    def update_tension_dynamic(self) -> None:
        """Update tension using emotion and relationship influence."""
        self.tension += (self.emotion / 10) * 0.9
        self.tension += self.calculate_relationship_tension()
        self.tension = max(0, min(1, self.tension))

    def make_moral_decision(self, situation: str) -> str:
        """Return a moral decision influenced by emotion and loyalty."""
        if self.emotional_state == "fearful":
            if self.tension > 0.7:
                decision = f"{self.name} decides to act selfishly, avoiding risk."
            else:
                decision = f"{self.name} helps others despite fear."
        elif self.emotional_state == "happy":
            decision = f"{self.name} helps others selflessly in {situation}."
        else:
            decision = f"{self.name} hesitates, torn between loyalty and personal interest."
        self.decisions_history.append(decision)
        return decision

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
