from typing import List
from .agent import Agent


class DynamicAgent(Agent):
    """Agent that can be dynamic or antidynamic."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, aktivnosti: int = 0,
                 agent_type: str = "dinami\u010den", active: bool = False):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.aktivnosti = aktivnosti
        self.agent_type = agent_type  # 'dinami\u010den' or 'antidinami\u010den'
        self.active = active
        self.connections: List[str] = []

    def transition(self) -> str:
        """Perform state transition based on type and thresholds."""
        if self.agent_type == "antidinami\u010den":
            self.state = "Ego"
            self.history.append(self.state)
            return self.state
        return super().transition()

    def komunikacija(self, drugi_agent: "DynamicAgent") -> str:
        """Simulate a line of dialogue influenced by current state."""
        line = f"{self.name} ({self.state}): {self.respond('Kaj je resnica?')}"
        # Interactions slightly raise emotion which may lead to transitions
        self.update_emotion(0.1)
        drugi_agent.update_emotion(0.1)
        return line

    def reorganiziraj(self, drugi_agent: "DynamicAgent") -> None:
        """Reorganize connections if dynamic and sufficiently active."""
        if self.agent_type == "dinami\u010den" and self.aktivnosti > 5:
            self.connections.append(drugi_agent.name)
            super().transition()
        elif self.agent_type == "antidinami\u010den":
            # Antidynamic agents do not reorganize
            pass


def dinamicka_inicializacija(agenti: List[DynamicAgent]) -> List[DynamicAgent]:
    """Connect active agents and trigger reorganization."""
    for i in range(len(agenti)):
        for j in range(i + 1, len(agenti)):
            a = agenti[i]
            b = agenti[j]
            if a.active and b.active:
                a.komunikacija(b)
                b.komunikacija(a)
                a.reorganiziraj(b)
                b.reorganiziraj(a)
    return agenti
