from __future__ import annotations
from typing import List

from .agent import Agent


class InteractionAgent(Agent):
    """Agent capable of basic interaction influenced by love and hate."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.interaction_history: List[str] = []

    def interact(self, other_agent: "InteractionAgent") -> str:
        """Interact with another agent based on emotional state."""
        if self.state == other_agent.state:
            if self.love > other_agent.love:
                outcome = "cooperate"
            else:
                outcome = "compete"
        else:
            if self.hate > other_agent.hate:
                outcome = "attack"
            else:
                outcome = "defend"

        self.interaction_history.append(outcome)
        other_agent.interaction_history.append(outcome)
        return outcome


class SimulationPhase:
    """Simple phase that can trigger a moral dilemma for an agent."""

    def __init__(self, phase_name: str, moral_dilemma: bool = False) -> None:
        self.phase_name = phase_name
        self.moral_dilemma = moral_dilemma

    def run(self, agent: Agent) -> None:
        if self.moral_dilemma:
            self.handle_moral_dilemma(agent)

    def handle_moral_dilemma(self, agent: Agent) -> None:
        if agent.love > agent.hate:
            decision = "choose love and cooperation"
        else:
            decision = "choose hate and aggression"
        agent.history.append(f"Moral decision: {decision}")


class AdvancedAgent(Agent):
    """Agent with advanced transitions influenced by emotion."""

    def transition(self) -> str:
        self.update_emotion()
        if self.emotion > 0.5 or self.tension > 0.7:
            if self.state == "Ego":
                self.state = "Jaz"
            elif self.state == "Jaz":
                self.state = "Enotnost"
        elif self.emotion < -0.5 and self.state == "Jaz":
            self.state = "Ego"
        self.history.append(f"Transitioned to: {self.state}")
        return self.state
