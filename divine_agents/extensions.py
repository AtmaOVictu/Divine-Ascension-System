"""Additional agent types and simulation utilities."""

from __future__ import annotations

import random
from typing import List

from .agent import Agent


class SimulationPhase:
    """Represents a phase in the simulation, optionally with a moral dilemma."""

    def __init__(self, name: str, moral_dilemma: bool = False) -> None:
        self.name = name
        self.moral_dilemma = moral_dilemma

    def run(self, agent: Agent) -> None:
        """Run the phase for a given agent."""
        if self.moral_dilemma:
            self.handle_moral_dilemma(agent)

    def handle_moral_dilemma(self, agent: Agent) -> None:
        if agent.state == "Ego":
            decision = "change" if agent.tension > 0.8 else "continue"
            agent.history.append(f"Moral dilemma decision: {decision}")


class LearningAgent(Agent):
    """Agent capable of learning from its past actions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.learning_history: List[str] = []

    def learn_from_past(self) -> None:
        if self.history:
            last_state = self.history[-1]
            self.learning_history.append(last_state)

    def adapt_to_environment(self) -> None:
        if self.learning_history:
            self.history.append(f"Adapting based on {self.learning_history[-1]}")


class InteractionAgent(Agent):
    """Agent capable of interacting with another agent."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.interaction_history: List[str] = []

    def interact(self, other: "InteractionAgent") -> str:
        if self.state == other.state:
            outcome = "cooperate"
        else:
            outcome = "compete"
        self.interaction_history.append(outcome)
        other.interaction_history.append(outcome)
        return outcome


class FreeWillAgent(Agent):
    """Agent that can make semi-random decisions."""

    def make_decision(self) -> str:
        decision = "bold" if random.random() > 0.5 else "cautious"
        self.history.append(f"Decision: {decision}")
        return decision
