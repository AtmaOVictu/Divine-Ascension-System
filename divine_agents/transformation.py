from .agent import Agent

class Transformation:
    """Forces an inevitable progression to the next state."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def enforce(self) -> str:
        """Increase tension so the agent must transition."""
        self.agent.update_tension(0.8)
        return self.agent.transition()
