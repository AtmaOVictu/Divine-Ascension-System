from typing import List
from .agent import Agent

class DynamicAgent(Agent):
    """Agent with dynamic or antidinamic behaviour."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, aktivnosti: int = 0, tip: str = "dinami\u010den"):
        super().__init__(name, state, tension, emotion)
        self.aktivnosti = aktivnosti
        self.povezave: List[Agent] = []
        self.tip = tip  # "dinami\u010den" or "antidinami\u010den"

    def prehod(self) -> str:
        """State transition based on agent type."""
        if self.tip == "dinami\u010den":
            return super().transition()
        # antidinamic agent stays in Ego regardless
        self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def komunikacija(self, drugi_agent: "DynamicAgent") -> None:
        """Communicate with another agent and possibly update state."""
        if self.tip == "dinami\u010den" and drugi_agent.state != self.state:
            self.update_emotion(0.3)
            self.prehod()

    def reorganiziraj(self, drugi_agent: "DynamicAgent") -> None:
        """Reorganize if activity threshold met."""
        if self.tip == "dinami\u010den" and self.aktivnosti > 5:
            self.povezave.append(drugi_agent)


def dinamicka_inicializacija(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Connect agents and trigger reorganization based on type."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            a = agenti[i]
            b = agenti[j]
            a.komunikacija(b)
            b.komunikacija(a)
            a.reorganiziraj(b)
            b.reorganiziraj(a)
    return agenti
