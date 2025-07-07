from typing import List
from .agent import Agent

class SubAgent:
    """Interface for sub-agents used by the Orchestrator."""

    def is_relevant(self, input_data: str) -> bool:
        """Return True if the agent should process the input."""
        raise NotImplementedError

    def process(self, input_data: str) -> str:
        """Process the input and return a response."""
        raise NotImplementedError


class OrchestratorAgent(Agent):
    """Top-level agent orchestrating sub-agents."""

    def __init__(self, name: str = "Orchestrator"):
        super().__init__(name=name)
        self.sub_agents: List[SubAgent] = []

    def add_sub_agent(self, agent: SubAgent) -> None:
        """Register a sub-agent for delegation."""
        self.sub_agents.append(agent)

    def run(self, input_data: str) -> str:
        """Delegate input to a relevant sub-agent if available."""
        for agent in self.sub_agents:
            if agent.is_relevant(input_data):
                return agent.process(input_data)
        return "No relevant agent found."
