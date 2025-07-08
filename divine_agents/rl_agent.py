from __future__ import annotations

"""Reinforcement learning agents with introspection abilities."""

from typing import Dict

from .agent import Agent


class RLAgent(Agent):
    """Agent enhanced with a simple Q-learning policy."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.0,
        learning_rate: float = 0.1,
        discount_factor: float = 0.9,
    ) -> None:
        super().__init__(name, state, tension, emotion)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table: Dict[str, Dict[str, float]] = {}

    def update_policy(self, state: str, action: str, reward: float, next_state: str) -> None:
        """Update internal Q-table using Q-learning."""
        self.q_table.setdefault(state, {}).setdefault(action, 0.0)
        self.q_table.setdefault(next_state, {})

        best_next = max(self.q_table[next_state].values(), default=0.0)
        td_target = reward + self.discount_factor * best_next
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_error


class ReflectiveAgent(RLAgent):
    """RL agent capable of self-reflection and emotional adjustment."""

    def __init__(
        self,
        name: str,
        state: str = "Ego",
        tension: float = 0.0,
        emotion: float = 0.5,
        learning_rate: float = 0.1,
        discount_factor: float = 0.9,
    ) -> None:
        super().__init__(name, state, tension, emotion, learning_rate, discount_factor)
        self.history: list[tuple[str, float, float]] = []

    def reflect(self, last_dialogue: str) -> None:
        """Adjust emotion and tension based on introspection."""
        if "fear" in last_dialogue or "anger" in last_dialogue:
            self.emotion *= 0.9
            self.tension = min(self.tension + 0.1, 1.0)
        self.history.append(("reflection", self.emotion, self.tension))

    def update_policy(self, state: str, action: str, reward: float, next_state: str) -> None:
        super().update_policy(state, action, reward, next_state)
        if reward > 0:
            self.emotion = min(self.emotion + 0.1, 1.0)
        else:
            self.emotion = max(self.emotion - 0.05, 0.0)

    def generate_response(self, user_input: str) -> str:
        """Generate a response influenced by the current emotional state."""
        prefix = "Let's continue the discussion calmly."
        if self.emotion > 0.7:
            prefix = "I am feeling positive about this!"
        elif self.emotion < 0.3:
            prefix = "I need to calm down before we continue."

        philosophical_part = self.respond(user_input)
        self.reflect(user_input)
        return f"{prefix} {philosophical_part}"


def reflective_dialogue(agent1: ReflectiveAgent, agent2: ReflectiveAgent) -> list[str]:
    """Simulate a dialogue using reflective agents."""
    lines: list[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.generate_response('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.generate_response('Kaj je resnica?')}")

    agent1.update_emotion(agent1.emotion + 0.3)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent2.emotion + 0.3)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.generate_response('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.generate_response('Kaj je resnica?')}")

    return lines
