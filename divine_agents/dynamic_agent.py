from __future__ import annotations
from typing import List
from .agent import Agent


class DynamicAgent(Agent):
    """Extended agent supporting communication and reorganization."""

    def __init__(self, name: str, state: str = "neutral", tension: float = 0.0,
                 emotion: float = 0.0, aktivnosti: int = 0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.aktivnosti = aktivnosti
        self.povezave: List[DynamicAgent] = []

    def komunikacija(self, drugi_agent: 'DynamicAgent') -> None:
        """Propagate activation state to another agent."""
        if self.state == "aktiviran":
            drugi_agent.state = "aktiviran"
        
    def reorganiziraj(self, drugi_agent: 'DynamicAgent') -> None:
        """Add a connection when activity threshold is met."""
        if self.aktivnosti > 5:
            self.state = "prehod"
            if self not in drugi_agent.povezave:
                drugi_agent.povezave.append(self)
            if drugi_agent not in self.povezave:
                self.povezave.append(drugi_agent)


def dinamicka_inicializacija(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Connect active agents and trigger reorganization."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            a = agenti[i]
            b = agenti[j]
            if a.state == "aktiviran" and b.state == "aktiviran":
                a.komunikacija(b)
                a.reorganiziraj(b)
                b.reorganiziraj(a)
    return agenti


def reorganizacija_sistema(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Increment activity and reorganize highly active agents."""
    for agent in agenti:
        agent.aktivnosti += 1
        if agent.aktivnosti > 10:
            agent.state = "reorganizirano"
    return agenti
