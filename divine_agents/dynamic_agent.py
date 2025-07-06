from __future__ import annotations
from typing import List
from .agent import Agent

class DynamicAgent(Agent):
    """Agent capable of dynamic or antidinamic behaviour."""

    def __init__(self, name: str, state: str = "aktiviran", tension: float = 0.0,
                 emotion: float = 0.0, aktivnosti: int = 0, tip: str = "dinamičen"):
        super().__init__(name, state="Ego", tension=tension, emotion=emotion)
        # override initial state (can be 'aktiviran')
        self.state = state
        self.history = [state]
        self.aktivnosti = aktivnosti
        self.connections: List[DynamicAgent] = []
        self.tip = tip

    def prehod(self) -> str:
        """Transition between states depending on agent type."""
        if self.tip == "dinamičen":
            # allow transition only if thresholds exceeded
            if self.state == "aktiviran":
                self.state = "Ego"
            if self.tension > 0.7 or self.emotion > 0.5:
                if self.state == "Ego":
                    self.state = "Jaz"
                elif self.state == "Jaz":
                    self.state = "Enotnost"
        else:
            # antidinamic agent keeps its state fixed as Ego
            self.state = "Ego"
        self.history.append(self.state)
        return self.state

    def komunikacija(self, drugi_agent: "DynamicAgent") -> None:
        """Interact with another agent, potentially affecting state."""
        if self.tip == "dinamičen" and drugi_agent.state == "aktiviran":
            if self.tension > 0.8:
                self.state = "Jaz"
            else:
                self.state = "Ego"
        else:
            # antidinamic agent does not modify behaviour
            pass

    def reorganiziraj(self, drugi_agent: "DynamicAgent") -> None:
        """Reorganize connections when activities exceed threshold."""
        if self.tip == "dinamičen":
            if self.aktivnosti > 5:
                self.state = "prehod"
                drugi_agent.connections.append(self)
        else:
            # antidinamic agent stays idle
            pass

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
            elif a.tip == "antidinamičen" and b.tip == "antidinamičen":
                print(f"Agent {a.name} in {b.name} sta antidinamična, njuni prehodi so fiksni.")
    return agenti
