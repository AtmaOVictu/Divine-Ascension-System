"""Automation utilities for Divine Ascension agents."""

from __future__ import annotations

import random
from typing import Dict, List, Optional

from .agent import Agent


class AutomatskiPrehodi:
    """Handle automatic state transitions for an agent."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def preveri_pogoje_za_prehod(self) -> str:
        """Trigger a transition if emotion or tension thresholds are met."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.transition()
        return self.agent.state


class SamodejnaOptimizacija:
    """Automatically adjust an agent after an error."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def optimiziraj_kodo(self) -> Agent:
        if "error" in self.agent.history:
            self.agent.tension = max(0.0, self.agent.tension - 0.1)
        return self.agent


class QLearningAgent:
    """Simple Q-learning helper for agents."""

    def __init__(self, actions: List[str], learning_rate: float = 0.1,
                 discount_factor: float = 0.9, epsilon: float = 0.1):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table: Dict[str, Dict[str, float]] = {}

    def get_action(self, state: str) -> str:
        if random.random() < self.epsilon or state not in self.q_table:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update_q_value(self, state: str, action: str, reward: float,
                       next_state: str) -> None:
        max_q = max(self.q_table.get(next_state, {}).values(), default=0)
        current_q = self.q_table.get(state, {}).get(action, 0)
        new_q = current_q + self.learning_rate * (
            reward + self.discount_factor * max_q - current_q
        )
        self.q_table.setdefault(state, {})[action] = new_q


class SamodejnoUcenje:
    """Wrapper to integrate Q-learning with an agent."""

    def __init__(self, agent: Agent, learner: QLearningAgent):
        self.agent = agent
        self.learner = learner

    def learn_from_experience(self, state: str, action: str, reward: float,
                              next_state: str) -> None:
        self.learner.update_q_value(state, action, reward, next_state)


class KolektivniModel:
    """Coordinate learning across multiple agents."""

    def __init__(self, agents: List[SamodejnoUcenje]):
        self.agents = agents

    def kolektivno_ucenje(self) -> None:
        for wrapper in self.agents:
            wrapper.learner.epsilon = max(0, wrapper.learner.epsilon - 0.01)


class PrelivanjeMedJeziki:
    """Translate expressions between two abstract languages."""

    def __init__(self, jezik1: str, jezik2: str):
        self.jezik1 = jezik1
        self.jezik2 = jezik2

    def prevedi(self, izraz: str) -> str:
        if self.jezik1 == "Filozofski" and self.jezik2 == "Matematicni":
            return f"Matematicna vrednost za: {self._filozofska_vrednost(izraz)}"
        return izraz

    def _filozofska_vrednost(self, izraz: str) -> int:
        if izraz == "absolutna resnica":
            return 1
        if izraz == "relativna resnica":
            return 0.5
        if izraz == "enotna resnica":
            return 0
        return 0


class SamodejnaRefaktorizacija:
    """Adjust agent tension based on errors in history."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def refaktoriziraj(self) -> Agent:
        if "error" in self.agent.history:
            self.agent.tension = max(0.0, self.agent.tension - 0.1)
        return self.agent
