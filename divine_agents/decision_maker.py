from __future__ import annotations
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - for type checking only
    from .agent import Agent


class DecisionMaker:
    """Handle state transitions and belief evolution for an agent."""

    def __init__(self, agent: 'Agent') -> None:
        self.agent = agent

    def decide_transition(self) -> str:
        """Decide the next state based on tension and emotion thresholds."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                self.agent.state = "Jaz"
            elif self.agent.state == "Jaz":
                self.agent.state = "Enotnost"
        self.agent.history.append(self.agent.state)
        return self.agent.state

    def evolve_beliefs(self) -> None:
        """Simple stochastic belief evolution."""
        outcome = random.choice(["optimistic", "pessimistic", "neutral"])
        self.agent.belief_system.append(outcome)
