from __future__ import annotations
from typing import Optional


class MetaparadoxicalModule:
    """Module handling paradoxical transitions for an agent."""

    def __init__(self, agent: "Agent") -> None:
        self.agent = agent

    def paradoxical_transition(self) -> str:
        """Perform a paradoxical transition based on the agent's state."""
        state_before = self.agent.state
        if self.agent.state == "Ego" and (
            self.agent.tension > 0.7 or self.agent.emotion > 0.5
        ):
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz" and (
            self.agent.tension > 0.7 or self.agent.emotion > 0.5
        ):
            self.agent.state = "Enotnost"
        # The module highlights contradiction by referencing previous state
        return f"{self.agent.name}: {state_before} -> {self.agent.state}"
