"""Logic for deciding agent state transitions and belief evolution."""
from __future__ import annotations

import random
from typing import List


class DecisionMaker:
    """Decision-making component for an agent."""

    def __init__(self, agent: "Agent"):
        self.agent = agent

    def decide_transition(self) -> str:
        """Return the next state for the agent based on thresholds."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                return "Jaz"
            if self.agent.state == "Jaz":
                return "Enotnost"
        return self.agent.state

    def evolve_beliefs(self) -> str:
        """Append a random belief to the agent's belief system."""
        belief = random.choice(["optimistic", "pessimistic", "neutral"])
        self.agent.belief_system.append(belief)
        return belief
