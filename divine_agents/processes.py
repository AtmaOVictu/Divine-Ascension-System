class Mediator:
    """Mediates between two agents to help resolve conflict and force state transitions."""
    def __init__(self, name: str):
        self.name = name

    def mediate(self, agent1, agent2):
        """Adjust agents' tension to encourage inevitable transitions."""
        if agent1.state == "Ego" and agent2.state in ("Jaz", "Enotnost"):
            agent1.update_tension(0.8)
            return agent1.transition()
        if agent1.state == "Jaz" and agent2.state == "Enotnost":
            agent1.update_tension(0.8)
            return agent1.transition()
        return agent1.state


class Meditacija:
    """Facilitates introspective meditation for an agent."""
    def __init__(self, agent):
        self.agent = agent

    def meditate(self):
        """Increase emotion to trigger an inevitable transition."""
        self.agent.update_emotion(0.6)
        return self.agent.transition()
