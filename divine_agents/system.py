from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue

class DynamicAgentSystem:
    """Manage multiple agents across ontological modules and run dialogues."""

    def __init__(self) -> None:
        self.modules = {state: [] for state in Agent.STATES}

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the system based on its current state."""
        self.modules[agent.state].append(agent)

    def _collect_agents(self) -> List[Agent]:
        agents = []
        for module_agents in self.modules.values():
            agents.extend(module_agents)
        return agents

    def _reassign(self, agents: List[Agent]) -> None:
        for module_agents in self.modules.values():
            module_agents.clear()
        for agent in agents:
            self.modules[agent.state].append(agent)

    def run_step(self) -> List[str]:
        """Run a single step of dialogues across all agent pairs."""
        lines: List[str] = []
        agents = self._collect_agents()
        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                lines.extend(philosophical_dialogue(agents[i], agents[j]))
        self._reassign(agents)
        return lines
