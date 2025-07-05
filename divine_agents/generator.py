class Generator:
    """Apply energy to agents to influence their transitions."""

    def __init__(self, power: float = 0.0, active: bool = False):
        self.power = power
        self.active = active

    def activate(self, power: float) -> None:
        """Activate the generator with a given power."""
        self.power = power
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the generator."""
        self.active = False

    def apply_to_agent(self, agent) -> None:
        """Modify an agent's emotion and tension based on generator power."""
        if not self.active:
            return
        increment = self.power
        agent.update_emotion(agent.emotion + increment)
        agent.update_tension(agent.tension + increment)
        agent.transition()
