from __future__ import annotations
from typing import List, Optional

from .agent import Agent

class InteractionAgent(Agent):
    """Agent with capability to record interactions."""

    def __init__(self, name: str, state: str = "Ego", **kwargs) -> None:
        super().__init__(name, state, **kwargs)
        self.interaction_history: List[str] = []

    def interact(self, other_agent: "InteractionAgent") -> str:
        """Interact with another agent based on love and hate levels."""
        if self.state == other_agent.state:
            outcome = "cooperate" if self.love > other_agent.hate else "compete"
        else:
            outcome = "attack" if self.hate > other_agent.hate else "defend"

        self.interaction_history.append(outcome)
        other_agent.interaction_history.append(outcome)
        return outcome


class SimulationPhase:
    """Represents a simulation phase that may include a moral dilemma."""

    def __init__(self, phase_name: str, moral_dilemma: bool = False) -> None:
        self.phase_name = phase_name
        self.moral_dilemma = moral_dilemma

    def run(self, agent: Agent) -> Optional[str]:
        if self.moral_dilemma:
            return self.handle_moral_dilemma(agent)
        return None

    def handle_moral_dilemma(self, agent: Agent) -> str:
        """Determine a decision for the agent when faced with a moral dilemma."""
        if agent.love > agent.hate:
            decision = "choose love and cooperation"
        else:
            decision = "choose hate and aggression"
        agent.history.append(f"Moral decision: {decision}")
        return decision


class AdvancedAgent(Agent):
    """Agent that updates emotion and performs complex transitions."""

    def transition(self) -> str:
        self.update_emotion()
        if self.emotion > 0.5:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        elif self.emotion < -0.5 and self.state == "Jaz":
            self.state = "Ego"
        self.history.append(self.state)
        return self.state
