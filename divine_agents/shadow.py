from __future__ import annotations

from dataclasses import dataclass

from .agent import Agent


@dataclass
class NujnaSenca:
    """Represents an urgent shadow influencing an agent."""

    name: str
    urgency: float

    def prehod_v_senco(self, agent: Agent) -> str:
        """Apply urgency to the agent and trigger a transition if needed."""
        if self.urgency >= 0.8:
            agent.update_tension(agent.tension + self.urgency)
        else:
            agent.update_tension(agent.tension + self.urgency / 2)
        return agent.transition()
