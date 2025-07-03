from __future__ import annotations
from typing import List

from .agent import Agent


class MoralAgent(Agent):
    """Agent with ethical decision-making capabilities."""

    def __init__(
        self,
        name: str,
        ethics: str = "utilitarianism",
        dimensions: int = 3,
        **kwargs,
    ) -> None:
        super().__init__(name, **kwargs)
        self.ethics = ethics
        self.dimensions = dimensions

    def moral_decision(self, other_agents: List["MoralAgent"]) -> str:
        """Return a moral decision based on the agent's ethical stance."""
        if self.ethics == "utilitarianism":
            return self._utilitarian_decision(other_agents)
        if self.ethics == "deontology":
            return self._deontological_decision()
        if self.ethics == "virtue":
            return self._virtue_decision()
        return self._justice_decision()

    def _utilitarian_decision(self, other_agents: List["MoralAgent"]) -> str:
        collective_emotion = sum(a.emotion for a in other_agents) + self.emotion
        collective_tension = sum(a.tension for a in other_agents) + self.tension
        if collective_emotion - collective_tension > 1:
            return "Maximize happiness for all"
        return "Minimize suffering for most"

    def _deontological_decision(self) -> str:
        return "Follow the rule no matter the consequences"

    def _virtue_decision(self) -> str:
        return "Act in accordance with virtues"

    def _justice_decision(self) -> str:
        return "Seek fair outcomes for all"

    def generate_shape(self) -> dict:
        """Return a simple representation of the agent's geometric shape."""
        shape = "circle" if self.dimensions <= 3 else "hypercube"
        return {"shape": shape, "dimensions": self.dimensions}
