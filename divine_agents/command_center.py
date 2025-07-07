from typing import List
from .agent import Agent

class CommandCenter:
    """Central controller that coordinates multiple agents."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents

    def execute_commands(self) -> List[str]:
        """Apply transitions across all agents and report changes."""
        reports = []
        for agent in self.agents:
            previous = agent.state
            agent.transition()
            if previous != agent.state:
                reports.append(f"{agent.name} prehaja iz {previous} v {agent.state}")
        return reports
