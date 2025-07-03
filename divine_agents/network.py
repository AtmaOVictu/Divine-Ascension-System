from typing import List
from .agent import Agent
from .dialogue import philosophical_dialogue

class Module:
    """Container for a group of agents working on a set of tasks."""

    def __init__(self, name: str):
        self.name = name
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to this module."""
        self.agents.append(agent)

    def run(self) -> List[str]:
        """Run the module tasks, increasing tension to trigger transitions."""
        results: List[str] = []
        for agent in self.agents:
            agent.update_tension(0.8)
            state = agent.transition()
            results.append(f"{agent.name} ({state}): {agent.respond('Kaj je resnica?')}")
        return results


class AgentNetwork:
    """Manage multiple modules and facilitate inter-module dialogue."""

    def __init__(self) -> None:
        self.modules: List[Module] = []

    def add_module(self, module: Module) -> None:
        self.modules.append(module)

    def bridge_dialogue(self) -> List[str]:
        """Initiate a dialogue between the first agents of the first two modules."""
        if len(self.modules) < 2:
            return []
        m1, m2 = self.modules[0], self.modules[1]
        if not m1.agents or not m2.agents:
            return []
        return philosophical_dialogue(m1.agents[0], m2.agents[0])
