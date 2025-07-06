"""Dynamic agent system module."""

from typing import List

from .agent import Agent


class DynamicAgentSystem:
    """Manage a collection of agents and simulate their interactions."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []

    def add_agent(self, agent: Agent) -> None:
        """Add an agent to the system."""
        self.agents.append(agent)

    def run_simulation(self) -> List[str]:
        """Run a basic simulation where each agent transitions once."""
        lines: List[str] = []

        for agent in self.agents:
            # Initial response in the current state
            lines.append(
                f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}"
            )

            # Increase emotion to trigger potential state change
            agent.update_emotion(0.6)
            lines.append(f"{agent.name} prehaja v stanje: {agent.transition()}")

        # Agents respond again from their new states
        for agent in self.agents:
            lines.append(f"{agent.name}: {agent.respond('Kaj je resnica?')}")

        return lines

