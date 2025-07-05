from __future__ import annotations
from typing import Dict, List

from .agent import Agent

class OntoAgent(Agent):
    """Agent with birth parameters and parental influence."""

    def __init__(self, name: str, birth_params: Dict[str, float], parent_params: Dict[str, float], state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, pathos: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.pathos = pathos
        self.birth_params = birth_params
        self.parent_params = parent_params

        self.tension += birth_params.get("initial_tension", 0.0)
        self.emotion += birth_params.get("initial_emotion", 0.0)
        self.apply_parental_influence()

    def apply_parental_influence(self) -> None:
        """Apply influence from parents to the agent's starting values."""
        self.tension += self.parent_params.get("parental_tension", 0.0)
        self.emotion += self.parent_params.get("parental_emotion", 0.0)
        self.pathos += self.parent_params.get("parental_pathos", 0.0)

    def adjust_pathos(self, external_factor: float) -> None:
        """Adjust pathos based on an external factor."""
        self.pathos += external_factor
        if self.pathos < 0:
            self.pathos = 0

    def optimize_transition(self) -> str:
        """Trigger a transition if thresholds are met."""
        if self.tension > 0.7 or self.emotion > 0.5 or self.pathos > 5:
            return self.transition()
        return self.state

    def respond(self, question: str) -> str:
        """Return a response influenced by the agent's emotion."""
        base = super().respond(question)
        if self.emotion > 0.7:
            feedback = "Močno čustvujem."
        elif self.emotion > 0.3:
            feedback = "Čustva rahlo vplivajo na moj odgovor."
        else:
            feedback = "Sem miren."
        return f"{base} {feedback}"


def dynamic_dialogue(agent1: OntoAgent, agent2: OntoAgent) -> List[str]:
    """Conduct a simple dialogue adjusting emotions and transitions."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(agent1.emotion + 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.optimize_transition()}")

    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.optimize_transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

