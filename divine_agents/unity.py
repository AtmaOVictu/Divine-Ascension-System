from typing import List
from .agent import Agent

class UnityCommand:
    """Ensure all agents operate under the command of Enotnost."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def enforce_unity(self) -> str:
        """Force all agents to transition towards Enotnost."""
        for agent in self.agents:
            while agent.state != "Enotnost":
                # escalate tension to surpass transition threshold
                agent.update_tension(1.0)
                agent.transition()
        return "Enotnost"

    def states(self) -> List[str]:
        """Return current states of managed agents."""
        return [agent.state for agent in self.agents]
