from .agent import Agent

class Mediator:
    """Coordinate transitions between agents through external guidance."""

    def __init__(self, name: str):
        self.name = name

    def mediate(self, agent1: Agent, agent2: Agent) -> str:
        """Adjust agent1 based on agent2's state to facilitate transition."""
        if agent1.state == "Ego" and agent2.state == "Jaz":
            agent1.update_emotion(0.6)
        elif agent1.state == "Jaz" and agent2.state == "Enotnost":
            agent1.update_emotion(0.6)
        return agent1.transition()


class Meditacija:
    """Internal reflection process leading to transformation."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def reflect(self) -> str:
        """Increase emotion to trigger the agent's transition."""
        self.agent.update_emotion(0.6)
        return self.agent.transition()


class Transformacija:
    """Force a transition through elevated tension."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def transform(self) -> str:
        """Elevate tension and perform transition."""
        self.agent.update_tension(0.8)
        return self.agent.transition()
