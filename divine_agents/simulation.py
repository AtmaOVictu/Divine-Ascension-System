from typing import Dict, List

from .agent import Agent


class SimulationEnvironment:
    """Environment to run transitions and track agent histories."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the simulation."""
        self.agents.append(agent)

    def run(self) -> None:
        """Run a single transition step for each agent."""
        for agent in self.agents:
            agent.transition()

    def histories(self) -> Dict[str, List[str]]:
        """Return the transition history for all agents."""
        return {agent.name: agent.history for agent in self.agents}
