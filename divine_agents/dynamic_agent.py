from typing import List

from .agent import Agent


class DynamicAgent(Agent):
    """Agent with optional dynamic or antidinamic behaviour."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, aktivnosti: int = 0,
                 tip: str = "dinamičen"):
        super().__init__(name, state, tension, emotion)
        self.aktivnosti = aktivnosti
        self.povezave: List["DynamicAgent"] = []
        self.tip = tip  # "dinamičen" or "antidinamičen"

    def transition(self) -> str:
        """Override transition to respect agent type."""
        if self.tip == "dinamičen":
            return super().transition()
        # antidinamičen agent does not change state
        self.history.append(self.state)
        return self.state

    def reorganiziraj(self, drugi_agent: "DynamicAgent") -> None:
        """Reorganise connections based on activity level for dynamic agents."""
        if self.tip == "dinamičen" and self.aktivnosti > 5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
            self.povezave.append(drugi_agent)

    def komunikacija(self, drugi_agent: "DynamicAgent") -> str:
        """Generate a short response when interacting with another agent."""
        if self.tip == "dinamičen" and drugi_agent.state in Agent.STATES:
            if self.tension > 0.8:
                self.update_emotion(0.1)
            return f"{self.name} komunicira z {drugi_agent.name}."
        return f"{self.name} (antidinamičen) ne reagira."


def dinamicka_inicializacija(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Connect active agents and trigger reorganization based on type."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            a = agenti[i]
            b = agenti[j]
            if a.tip == "dinamičen" and b.tip == "dinamičen":
                if a.state in Agent.STATES and b.state in Agent.STATES:
                    a.komunikacija(b)
                    a.reorganiziraj(b)
                    b.reorganiziraj(a)
            elif a.tip == "antidinamičen" and b.tip == "antidinamičen":
                print(f"Agent {a.name} in {b.name} sta antidinamična, njuni prehodi so fiksni.")
    return agenti
