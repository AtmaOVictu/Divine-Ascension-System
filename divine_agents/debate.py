from dataclasses import dataclass
from typing import Tuple

from .agent import Agent


@dataclass
class Debate:
    """Simulate a dialogue exchange between two agents."""

    agent1: Agent
    agent2: Agent

    def step(self) -> Tuple[str, str]:
        """Perform one exchange of dialogue and update agent states."""
        self.agent1.update_state()
        self.agent2.update_state()
        return self.agent1.respond(), self.agent2.respond()
