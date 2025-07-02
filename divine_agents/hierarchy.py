from typing import List

from .agent import Agent


class MainAgent(Agent):
    """Agent that can manage a list of subagents."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, materials=None) -> None:
        super().__init__(name, state, tension, emotion, materials)
        self.sub_agents: List[Agent] = []

    def create_sub_agent(self, name: str, state: str = "Ego",
                          tension: float = 0.0, emotion: float = 0.0,
                          materials=None) -> Agent:
        """Create a subagent controlled by this agent."""
        sub = Agent(name, state, tension, emotion, materials)
        self.sub_agents.append(sub)
        return sub

    def transition_sub_agents(self) -> None:
        """Trigger transitions for all subagents based on their thresholds."""
        for sub in self.sub_agents:
            sub.transition()
