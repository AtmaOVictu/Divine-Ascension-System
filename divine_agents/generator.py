# Generator module for ontological system
from __future__ import annotations

from .agent import Agent


class Generator:
    """Ontological generator that amplifies energy and guides transitions."""

    def __init__(self, active: bool = False) -> None:
        self.active = active
        self.energy = 0.0

    def activate(self) -> None:
        """Activate generator and start producing energy."""
        self.active = True
        self.energy = 1.0

    def energize(self, agent: Agent, amount: float) -> str:
        """Increase agent tension and emotion, potentially triggering a transition."""
        if not self.active:
            return agent.state

        # Increase agent's internal states
        agent.update_tension(agent.tension + amount * self.energy)
        agent.update_emotion(agent.emotion + amount * 0.5)
        return agent.transition()

    @staticmethod
    def meaning() -> str:
        """Explain generator according to the ontological framework."""
        return (
            "Generator prebuja potencial in usmerja prehode skozi faze, "
            "omogočajoč dinamično transformacijo sistema."
        )
