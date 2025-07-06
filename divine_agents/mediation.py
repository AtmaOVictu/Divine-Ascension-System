from .agent import Agent

class Mediator:
    """Facilitates transitions between agents when conflicts arise."""

    def __init__(self, name: str):
        self.name = name

    def mediate(self, agent1: Agent, agent2: Agent) -> str:
        """Adjust tension so agent1 can progress toward agent2's state."""
        if agent1.state == "Ego" and agent2.state == "Jaz":
            agent1.update_tension(0.8)
        elif agent1.state == "Jaz" and agent2.state == "Enotnost":
            agent1.update_tension(0.8)
        return agent1.transition()
