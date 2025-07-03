from __future__ import annotations
from typing import List

from .agent import Agent


class MoralAgent(Agent):
    """Agent with moral decision-making abilities."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, ethics: str = "utilitarianism"):
        super().__init__(name, state, tension, emotion)
        self.ethics = ethics
        self.decision: str | None = None

    def utilitarian_decision(self, others: List[Agent]) -> str:
        collective_emotion = sum(agent.emotion for agent in others)
        collective_tension = sum(agent.tension for agent in others)
        if collective_emotion - collective_tension > 1:
            return "Maximize happiness for all"
        return "Minimize suffering for most"

    def deontological_decision(self) -> str:
        return "Follow the rule no matter the consequences"

    def moral_decision(self, others: List[Agent]) -> str:
        if self.ethics == "deontology":
            self.decision = self.deontological_decision()
        else:
            self.decision = self.utilitarian_decision(others)
        return self.decision

    def reflect(self, others: List[Agent]) -> str:
        self.transition()
        decision = self.moral_decision(others)
        return f"{self.name} sprejema odločitev: {decision}. Stanje: {self.state}"
