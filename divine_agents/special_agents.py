from __future__ import annotations

from typing import Dict, List

from .agent import Agent


class LogicAgent(Agent):
    """Agent capable of logical reasoning using stored facts."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.facts: Dict[str, bool] = {}
        self.conclusions: List[str] = []

    def add_fact(self, fact: str, value: bool) -> None:
        """Store a fact with its truth value."""
        self.facts[fact] = value

    def evaluate(self, condition: str) -> bool | None:
        """Evaluate a condition and store the conclusion."""
        if condition in self.facts:
            decision = self.facts[condition]
            self.conclusions.append(f"Condition {condition} is {decision}.")
            return decision
        return None

    def get_conclusions(self) -> List[str]:
        return self.conclusions


class ConfirmationAgent(Agent):
    """Agent that verifies and confirms facts or decisions."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.verified_facts: List[str] = []

    def confirm_fact(self, fact: str, value: bool) -> None:
        self.verified_facts.append(fact)

    def verify_decision(self, decision: str) -> bool:
        if decision in self.verified_facts:
            return True
        return False


class DeconfirmationAgent(Agent):
    """Agent that challenges and attempts to disprove facts."""

    def __init__(self, name: str, state: str = "Ego") -> None:
        super().__init__(name, state)
        self.challenged_facts: List[str] = []

    def challenge_fact(self, fact: str) -> None:
        self.challenged_facts.append(fact)

    def deconfirm_fact(self, fact: str) -> str:
        if fact in self.challenged_facts:
            return f"Deconfirmation of {fact} successful"
        return f"{fact} has not been challenged yet."
