from __future__ import annotations
from typing import List


class DynamicAgent:
    """Agent capable of dynamic state transitions and reorganization."""

    STATES = ("Ego", "Jaz", "Enotnost")

    def __init__(self, ime: str, stanje: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, aktivnosti: int = 0) -> None:
        self.ime = ime
        self.stanje = stanje
        self.tension = tension
        self.emotion = emotion
        self.aktivnosti = aktivnosti
        self.povezave: List[DynamicAgent] = []

    def prehod(self) -> str:
        """Transition between ontological states based on thresholds."""
        if self.tension > 0.7:
            if self.stanje == "Ego":
                self.stanje = "Jaz"
            elif self.stanje == "Jaz":
                self.stanje = "Enotnost"
        elif self.emotion > 0.5:
            if self.stanje == "Ego":
                self.stanje = "Jaz"
            elif self.stanje == "Jaz":
                self.stanje = "Enotnost"
        return self.stanje

    def komunikacija(self, drugi_agent: "DynamicAgent") -> None:
        """Communicate and align states if agent is not in Ego."""
        if self.stanje != "Ego":
            drugi_agent.stanje = self.stanje
            if self not in drugi_agent.povezave:
                drugi_agent.povezave.append(self)
            if drugi_agent not in self.povezave:
                self.povezave.append(drugi_agent)

    def reorganiziraj(self, drugi_agent: "DynamicAgent") -> None:
        """Automatically reorganize when activity threshold is exceeded."""
        if self.aktivnosti > 5:
            self.prehod()
            if self not in drugi_agent.povezave:
                drugi_agent.povezave.append(self)


def dinamicka_inicializacija(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Dynamically connect active agents."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            if agenti[i].stanje != "Ego" and agenti[j].stanje != "Ego":
                agenti[i].komunikacija(agenti[j])
                agenti[i].reorganiziraj(agenti[j])
                agenti[j].reorganiziraj(agenti[i])
    return agenti


def reorganizacija_sistema(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Increment activity and reorganize highly active agents."""
    for agent in agenti:
        agent.aktivnosti += 1
        if agent.aktivnosti > 10:
            agent.stanje = "reorganizirano"
    return agenti
