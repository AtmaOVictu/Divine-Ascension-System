from .agent import Agent

class InterpolationAgent(Agent):
    """Agent that connects different states or ideas by interpolation."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, interpolation_level: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.interpolation_level = interpolation_level

    def interpolate(self, agent1: Agent, agent2: Agent) -> str:
        """Attempt to interpolate between two agents."""
        if self.interpolation_level > 0.5:
            return f"Interpoliram med {agent1.state} in {agent2.state}: možna je povezava."
        return f"Ne morem interpolirati med {agent1.state} in {agent2.state}."
