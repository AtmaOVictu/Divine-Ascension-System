from __future__ import annotations
from typing import List, Optional

from .agent import Agent


class OppositeAgent(Agent):
    """Represents an agent embodying a concept opposite to another agent."""

    def __init__(self, name: str, concept: str, state: str = "Ego"):
        super().__init__(name, state=state)
        self.concept = concept

    def activate_opposite(self, agent: 'OntologicalAgent') -> List[str]:
        """Activate debate with the provided agent."""
        return agent.debate()


class OntologicalAgent(Agent):
    """Agent capable of debating with its opposite."""

    def __init__(self, name: str, concept: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.concept = concept
        self.opposite: Optional[OppositeAgent] = None

    def define_opposite(self, opposite: OppositeAgent) -> None:
        """Assign an opposite agent."""
        self.opposite = opposite

    def debate(self) -> List[str]:
        """Perform a debate with the opposite agent and handle transitions."""
        if not self.opposite:
            return []

        lines = [
            f"{self.name} in {self.opposite.name} ustvarjata dialekti\u010dno napetost.",
            f"{self.name}: {self.respond('Kaj je resnica?')}",
            f"{self.opposite.name}: {self.opposite.respond('Kaj je resnica?')}"
        ]
        # Increase emotions to trigger possible transitions
        self.update_emotion(0.8)
        self.opposite.update_emotion(0.6)
        lines.append(f"{self.name} prehaja v stanje: {self.transition()}")
        lines.append(f"{self.opposite.name} prehaja v stanje: {self.opposite.transition()}")
        lines.append(f"{self.name}: {self.respond('Kaj je resnica?')}")
        lines.append(f"{self.opposite.name}: {self.opposite.respond('Kaj je resnica?')}")
        return lines
