from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue

class Module:
    """A container linking agents to an ontological phase."""

    def __init__(self, name: str, phase: str):
        self.name = name
        self.phase = phase
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to this module if not already present."""
        if agent not in self.agents:
            self.agents.append(agent)

    def execute(self) -> List[str]:
        """Execute the module, triggering agent transitions and responses."""
        lines: List[str] = []
        for agent in self.agents:
            agent.transition()
            lines.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
        return lines


class AgentNetwork:
    """Manage modules and coordinate their interactions."""

    def __init__(self):
        self.modules: List[Module] = []

    def add_module(self, module: Module) -> None:
        """Register a new module in the network."""
        self.modules.append(module)

    def simulate(self) -> List[str]:
        """Simulate a simple dialogue between the first agents of two modules."""
        if len(self.modules) < 2:
            return []
        m1, m2 = self.modules[:2]
        if not m1.agents or not m2.agents:
            return []
        return philosophical_dialogue(m1.agents[0], m2.agents[0])
