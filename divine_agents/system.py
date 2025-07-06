"""Dynamic system handling multiple agents across positions."""
from typing import List
from .agent import Agent


class DynamicAgentSystem:
    """Manage a collection of agents and run a simulation."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Register an agent with the system."""
        self.agents.append(agent)

    def run_simulation(self) -> List[str]:
        """Run a simple simulation where each agent transitions."""
        transcript = []
        for agent in self.agents:
            transcript.append(f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}")
            agent.update_emotion(0.6)
            transcript.append(f"{agent.name} prehaja v stanje: {agent.transition()}")
            transcript.append("")
        return transcript
