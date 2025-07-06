from __future__ import annotations
import random
from typing import List
from .agent import Agent


class AutomatskiPrehodi:
    """Handle automatic state transitions for an agent."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def preveri_pogoje_za_prehod(self) -> str:
        """Change the agent state based on tension, emotion and history."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            if self.agent.state == "Ego":
                self.agent.state = "Jaz"
            elif self.agent.state == "Jaz":
                self.agent.state = "Enotnost"
        if "selfish" in self.agent.history:
            self.agent.state = "Enotnost"
        self.agent.history.append(self.agent.state)
        return self.agent.state


class SamodejnaOptimizacija:
    """Basic error recovery and optimisation helper."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def optimiziraj_kodo(self) -> Agent:
        if "error" in self.agent.history:
            self.agent.tension = max(0.0, self.agent.tension - 0.1)
        return self.agent


class QLearningAgent(Agent):
    """Agent with simple Q-learning capabilities."""

    def __init__(self, name: str, actions: List[str], learning_rate: float = 0.1,
                 discount_factor: float = 0.9, epsilon: float = 0.1, **kwargs):
        super().__init__(name, **kwargs)
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table: dict[str, dict[str, float]] = {}

    def get_action(self, state: str) -> str:
        if random.random() < self.epsilon or state not in self.q_table:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update_q_value(self, state: str, action: str, reward: float, next_state: str) -> None:
        self.q_table.setdefault(state, {})
        self.q_table.setdefault(next_state, {})
        max_q = max(self.q_table[next_state].values(), default=0)
        current_q = self.q_table[state].get(action, 0)
        self.q_table[state][action] = current_q + self.learning_rate * (
            reward + self.discount_factor * max_q - current_q
        )


class SamodejnoUcenje:
    """Wrapper for learning from experience using Q-learning."""

    def __init__(self, agent: QLearningAgent):
        self.agent = agent

    def learn_from_experience(self, state: str, action: str, reward: float, next_state: str) -> None:
        self.agent.update_q_value(state, action, reward, next_state)


class KolektivniModel:
    """Group model that aggregates learning across agents."""

    def __init__(self, agents: List[QLearningAgent]):
        self.agents = agents

    def kolektivno_ucenje(self, experiences: List[tuple[QLearningAgent, str, str, float, str]]) -> None:
        for agent, state, action, reward, next_state in experiences:
            agent.update_q_value(state, action, reward, next_state)
