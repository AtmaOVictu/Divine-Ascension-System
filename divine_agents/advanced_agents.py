from __future__ import annotations

import random
from .agent import Agent


class LearningAgent(Agent):
    """Agent that stores past transitions to adapt its behaviour."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.learning_history = []

    def learn_from_past(self) -> str | None:
        """Remember the last transition in learning history."""
        if self.history:
            last = self.history[-1]
            self.learning_history.append(last)
            return last
        return None

    def adapt_to_environment(self) -> str | None:
        """Simple adaptation based on the latest learned state."""
        if self.learning_history:
            return self.learning_history[-1]
        return None


class InteractionAgent(Agent):
    """Agent capable of interacting with other agents."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.interaction_history = []

    def interact(self, other: "InteractionAgent") -> str:
        if self.state == other.state:
            outcome = "cooperate"
        else:
            outcome = "compete"
        self.interaction_history.append(outcome)
        other.interaction_history.append(outcome)
        return outcome


class FreeWillAgent(Agent):
    """Agent that can make random decisions representing free will."""

    def make_decision(self) -> str:
        decision_point = random.random()
        decision = "bold" if decision_point > 0.5 else "cautious"
        self.history.append(f"Free will decision: {decision}")
        return decision
