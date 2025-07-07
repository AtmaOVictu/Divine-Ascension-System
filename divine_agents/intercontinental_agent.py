from .agent import Agent

class IntercontinentalizationAgent(Agent):
    """Agent that connects agents across different ontological realms."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, reach: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.reach = reach

    def connect_worlds(self, agent1: Agent, agent2: Agent) -> str:
        """Attempt to connect two agents across dimensional boundaries."""
        if self.reach > 0.5:
            return f"Povezujem {agent1.state} in {agent2.state} prek dimenzij."
        return f"Nezadosen doseg za povezavo {agent1.state} in {agent2.state}."
