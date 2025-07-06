from __future__ import annotations

from .agent import Agent


class Mediator:
    """Facilitates balance between two agents and triggers transitions."""

    def __init__(self, name: str):
        self.name = name

    def mediate(self, agent1: Agent, agent2: Agent) -> str:
        """Mediate between agents and adjust agent1 state if needed."""
        if agent1.state == "Ego" and agent2.state == "Jaz":
            agent1.update_tension(0.8)
            state = agent1.transition()
            return f"{self.name} mediates: {agent1.name} transitions to {state}"
        if agent1.state == "Jaz" and agent2.state == "Enotnost":
            agent1.update_tension(0.8)
            state = agent1.transition()
            return f"{self.name} mediates: {agent1.name} transitions to {state}"
        return f"{self.name}: No transition"


class Meditation:
    """Represents an introspective process for an agent."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def meditate(self) -> str:
        """Increase emotion to provoke a potential transition."""
        self.agent.update_emotion(0.6)
        state = self.agent.transition()
        return f"{self.agent.name} meditates and reaches {state}"


class Transformacija:
    """Ensures inevitable progress to a higher state."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def transform(self) -> str:
        """Force transition by raising tension beyond the threshold."""
        self.agent.update_tension(1.0)
        state = self.agent.transition()
        return f"{self.agent.name} is transformed to {state}"
