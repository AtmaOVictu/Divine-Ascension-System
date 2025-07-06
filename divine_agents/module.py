from typing import List

from .agent import Agent


class AgentModule:
    """Group multiple agents operating within a single module or position."""

    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to this module."""
        self.agents.append(agent)

    def dialogue_with(self, other: "AgentModule", question: str) -> List[str]:
        """Run a dialogue between agents of two modules."""
        lines: List[str] = []
        max_len = max(len(self.agents), len(other.agents))
        for i in range(max_len):
            if i < len(self.agents):
                a = self.agents[i]
                lines.append(f"{a.name} ({self.name}/{a.state}): {a.respond(question)}")
                a.update_emotion(0.6)
                a.transition()
                lines.append(f"{a.name} prehaja v stanje: {a.state}")
            if i < len(other.agents):
                b = other.agents[i]
                lines.append(f"{b.name} ({other.name}/{b.state}): {b.respond(question)}")
                b.update_emotion(0.6)
                b.transition()
                lines.append(f"{b.name} prehaja v stanje: {b.state}")
        return lines
