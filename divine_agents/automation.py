from __future__ import annotations
import random
from typing import List, Dict

from .agent import Agent


class AutomatskiPrehodi:
    """Automatically manage agent state transitions."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def preveri_pogoje_za_prehod(self) -> str:
        """Check conditions and trigger transition if thresholds are met."""
        if self.agent.tension > 0.7 or self.agent.emotion > 0.5:
            self.agent.transition()
        return self.agent.state


class SamodejnaOptimizacija:
    """Automatically optimize agent after errors."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def optimiziraj_kodo(self) -> Agent:
        """Reduce tension when an error is detected in history."""
        if "error" in self.agent.history:
            self.agent.tension = max(0.0, self.agent.tension - 0.1)
        return self.agent


class QLearningAgent(Agent):
    """Agent with Q-learning capabilities."""

    def __init__(self, name: str, actions: List[str], **kwargs):
        super().__init__(name, **kwargs)
        self.actions = actions
        self.learning_rate = kwargs.get("learning_rate", 0.1)
        self.discount_factor = kwargs.get("discount_factor", 0.9)
        self.epsilon = kwargs.get("epsilon", 0.1)
        self.q_table: Dict[str, Dict[str, float]] = {}
        self.last_action: str | None = None

    def get_action(self, state: str) -> str:
        if random.uniform(0, 1) < self.epsilon:
            action = random.choice(self.actions)
        else:
            state_actions = self.q_table.get(state, {})
            if state_actions:
                action = max(state_actions, key=state_actions.get)
            else:
                action = random.choice(self.actions)
        self.last_action = action
        return action

    def update_q_value(self, state: str, action: str, reward: float, next_state: str) -> None:
        max_q = max(self.q_table.get(next_state, {}).values(), default=0)
        current_q = self.q_table.get(state, {}).get(action, 0)
        updated = current_q + self.learning_rate * (reward + self.discount_factor * max_q - current_q)
        self.q_table.setdefault(state, {})[action] = updated


class SamodejnoUcenje:
    """Utility for automatic learning of agents using Q-learning."""

    def __init__(self, agent: QLearningAgent):
        self.agent = agent

    def learn_from_experience(self, state: str, action: str, reward: float, next_state: str) -> None:
        self.agent.update_q_value(state, action, reward, next_state)


class KolektivniModel:
    """Group model allowing agents to learn collectively."""

    def __init__(self, agents: List[QLearningAgent]):
        self.agents = agents

    def kolektivno_ucenje(self) -> None:
        for agent in self.agents:
            if agent.last_action:
                agent.update_q_value(agent.state, agent.last_action, 0, agent.state)

