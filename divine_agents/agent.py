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


class MembershipAgent(Agent):
    """Agent capable of joining groups and adapting based on environment."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, group: str | None = None):
        super().__init__(name, state, tension, emotion)
        self.group = group

    def ionize_environment(self, other_agent: "MembershipAgent") -> bool:
        """Simulate ionization and join other's group if thresholds are high."""
        if self.tension > 0.8 or self.emotion > 0.7:
            self.group = getattr(other_agent, "group", other_agent)
            return True
        return False

    def transition(self) -> str:
        """Ionize environment then perform state transition."""
        self.ionize_environment(self)
        return super().transition()


class InterpretiveAgent(MembershipAgent):
    """Agent that interprets changes and aligns with others."""

    def interpret_change(self, other_agent: Agent) -> str:
        """Adopt state of another agent based on its ontological stance."""
        if other_agent.state == "Enotnost":
            self.state = "Enotnost"
        elif other_agent.state == "Jaz":
            self.state = "Jaz"
        return self.state
