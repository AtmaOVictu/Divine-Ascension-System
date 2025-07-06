class MultiAgentSystem:
    """A system managing multiple agents and their interactions."""

    def __init__(self) -> None:
        self.agents = []

    def add_agent(self, agent):
        self.agents.append(agent)

    def interact(self) -> list[str]:
        """Simple interaction where each agent shares its view."""
        lines = []
        for agent in self.agents:
            lines.append(f"{agent.name}: {agent.respond('Kaj je resnica?')}")
            agent.update_emotion(0.3)
        return lines

