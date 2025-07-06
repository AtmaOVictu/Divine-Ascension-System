class EmotionalContagion:
    """Manage emotional contagion between multiple agents."""

    def __init__(self):
        self.agents = []

    def add_agent(self, agent):
        """Register an agent into the contagion system."""
        self.agents.append(agent)

    def spread_emotion(self, agent_index: int, influence: float) -> None:
        """Spread an agent's emotion to others with additional influence."""
        source = self.agents[agent_index]
        for i, other in enumerate(self.agents):
            if i != agent_index:
                other.update_emotion(source.emotion + influence)

