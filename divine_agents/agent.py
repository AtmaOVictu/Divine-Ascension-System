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

    def emotional_respond(self, question: str) -> str:
        """Return a response influenced by the agent's emotion level."""
        base = self.respond(question)
        if self.emotion > 0.5:
            return f"{base} (odziv čustveno)"
        return f"{base} (odziv mirno)"


class ReasonAgent(Agent):
    """Agent that reasons based on a logic level."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, logic_level: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.logic_level = logic_level

    def update_logic(self, value: float) -> None:
        """Increase logic level up to a maximum of 1.0."""
        self.logic_level = min(self.logic_level + value, 1.0)

    def reason(self, context: str) -> str:
        """Provide a logical deduction based on the logic level."""
        if self.logic_level > 0.5:
            return (f"Analyzing context '{context}' logically: Reason dictates "
                    "that this is a valid interpretation.")
        return (f"Reasoning insufficient to conclude for context '{context}'. "
                "Further analysis required.")


class InterpolationAgent(Agent):
    """Agent that connects disparate ideas or states."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, interpolation_level: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.interpolation_level = interpolation_level

    def interpolate(self, agent1: Agent, agent2: Agent) -> str:
        """Bridge two agent states if interpolation level is high enough."""
        if self.interpolation_level > 0.5:
            return (f"Interpolating between {agent1.state} and {agent2.state}: "
                    "A connection is possible.")
        return (f"Unable to interpolate between {agent1.state} and "
                f"{agent2.state}: Insufficient interpolation capacity.")


class IntercontinentalizationAgent(Agent):
    """Agent capable of connecting different ontological realms."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, reach: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.reach = reach

    def connect_worlds(self, agent1: Agent, agent2: Agent) -> str:
        """Connect two agents across conceptual boundaries."""
        if self.reach > 0.5:
            return (f"Connecting {agent1.state} and {agent2.state} across "
                    "dimensional boundaries.")
        return (f"Unable to connect {agent1.state} and {agent2.state}: "
                "Insufficient reach.")
