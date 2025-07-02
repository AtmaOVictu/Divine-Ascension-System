"""Advanced agent behaviors including mutation, permutation, inspiration, and ethical challenges."""

from __future__ import annotations

import random
from dataclasses import dataclass
from typing import List

from .agent import Agent


class MutatingAgent(Agent):
    """Agent capable of mutating its state and philosophical school."""

    PHILOSOPHICAL_SCHOOLS = [
        "Nihilizem",
        "Stoicizem",
        "Empirizem",
        "Idealizem",
        "Eksistencializem",
    ]

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, philosophy: str = "Stoicizem"):
        super().__init__(name, state, tension, emotion)
        self.philosophy = philosophy

    def mutate(self) -> None:
        """Randomly change state and philosophy with a 30% chance."""
        if random.random() < 0.3:
            self.state = random.choice(self.STATES)
            self.philosophy = random.choice(self.PHILOSOPHICAL_SCHOOLS)

    def respond(self, question: str) -> str:
        base = super().respond(question)
        if self.state == "Ego":
            return f"Mutirani Ego odgovor: {base}"
        if self.state == "Jaz":
            return f"Mutirani Jaz odgovor: {base}"
        return f"Mutirani Enotnost odgovor: {base}"


@dataclass
class PermutingAgent:
    """Utility for swapping attributes between two agents."""

    agent1: MutatingAgent
    agent2: MutatingAgent

    def permute(self) -> None:
        self.agent1.state, self.agent2.state = self.agent2.state, self.agent1.state
        self.agent1.philosophy, self.agent2.philosophy = (
            self.agent2.philosophy,
            self.agent1.philosophy,
        )


class InspirationalAgent(Agent):
    """Agent that can inspire another agent to change state and philosophy."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, inspiration: bool = False):
        super().__init__(name, state, tension, emotion)
        self.inspiration = inspiration

    def inspire(self, other: MutatingAgent) -> None:
        if not self.inspiration:
            return
        other.state = "Enotnost" if other.state == "Ego" else "Jaz"
        other.philosophy = random.choice(MutatingAgent.PHILOSOPHICAL_SCHOOLS)


@dataclass
class EthicalChallenge:
    """Moral choice affecting an agent's state."""

    dilemma: str
    options: List[str]
    agent: Agent

    def present(self) -> str:
        decision = self.choose_option()
        self.apply_decision(decision)
        return decision

    def choose_option(self) -> str:
        if self.agent.state == "Ego":
            return self.options[0]
        if self.agent.state == "Jaz":
            return self.options[1]
        return self.options[0]

    def apply_decision(self, decision: str) -> None:
        if decision == "Svoboda":
            self.agent.state = "Ego"
        else:
            self.agent.state = "Enotnost"
