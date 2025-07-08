from __future__ import annotations

from typing import Iterable, List

from .agent import Agent
from .special_agents import LogicAgent, ConfirmationAgent, DeconfirmationAgent


class MultiAgentSystem:
    """Coordinate interactions between various agents."""

    def __init__(self, agents: Iterable[Agent]):
        self.agents: List[Agent] = list(agents)

    def start_interaction(self) -> None:
        """Trigger a simple interaction among agents."""
        for agent in self.agents:
            if isinstance(agent, LogicAgent):
                agent.evaluate("earth_is_round")
            elif isinstance(agent, ConfirmationAgent):
                agent.verify_decision("earth_is_round")
            elif isinstance(agent, DeconfirmationAgent):
                agent.challenge_fact("earth_is_round")
                agent.deconfirm_fact("earth_is_round")

            # increase emotion to force possible transitions
            agent.update_emotion(0.8)
            agent.transition()

    def check_agents_status(self) -> List[str]:
        status = []
        for agent in self.agents:
            line = f"{agent.name} - State: {agent.state}"
            status.append(line)
        return status
