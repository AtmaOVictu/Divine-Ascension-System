"""System for managing ontological agent transitions in cycles."""
from typing import Dict, List

from .agent import Agent


class OntologicalSystem:
    """Manage multiple agents and record their transition cycles."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.data: List[Dict[str, object]] = []

    def add_agent(self, agent: Agent) -> None:
        """Register a new agent in the system."""
        self.agents.append(agent)

    def cycle(self) -> None:
        """Advance all agents by one transition and store the result."""
        for agent in self.agents:
            previous_state = agent.state
            new_state = agent.transition()
            self.data.append(
                {
                    "name": agent.name,
                    "from": previous_state,
                    "to": new_state,
                    "tension": agent.tension,
                    "emotion": agent.emotion,
                }
            )

    def run(self, steps: int) -> None:
        """Run multiple cycles of transitions."""
        for _ in range(steps):
            self.cycle()

    def history(self) -> List[Dict[str, object]]:
        """Return collected transition data."""
        return self.data
