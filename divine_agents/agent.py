class Agent:
    """Represents an ontological agent capable of transitioning states."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        self.name = name
        self.state = state
        self.tension = tension
        self.emotion = emotion
        self.history = [state]

    def update_emotion(self, value: float) -> None:
        """Update emotion intensity and adjust tension accordingly."""
        self.emotion = value
        self.tension += value

    def update_tension(self, value: float) -> None:
        """Directly set tension level."""
        self.tension = value

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


class MultiDimensionalMoralAgent(Agent):
    """Agent with moral reasoning and dimensional awareness."""

    ETHICS = ("utilitarianism", "deontology", "virtue", "justice")

    def __init__(self, name: str, ethics: str = "utilitarianism",
                 state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, dimensions: int = 3):
        super().__init__(name, state, tension, emotion)
        self.ethics = ethics
        self.dimensions = dimensions

    # Moral decision methods
    def moral_decision(self, other_agents: list[Agent] | None = None) -> str:
        """Return a moral decision string based on the agent's ethics."""
        other_agents = other_agents or []
        if self.ethics == "utilitarianism":
            return self._utilitarian_decision(other_agents)
        if self.ethics == "deontology":
            return "Follow the rule no matter the consequences"
        if self.ethics == "virtue":
            return "Act in accordance with virtues like honesty and courage"
        return "Seek fair and just outcomes for all involved"

    def _utilitarian_decision(self, other_agents: list[Agent]) -> str:
        """Private helper for utilitarian reasoning."""
        collective_emotion = self.emotion + sum(a.emotion for a in other_agents)
        collective_tension = self.tension + sum(a.tension for a in other_agents)
        if collective_emotion >= collective_tension:
            return "Maximize happiness for all"
        return "Minimize suffering for most"
