from __future__ import annotations

from typing import Dict, Tuple

from .agent import Agent


class RLAgent(Agent):
    """Agent with simple Q-learning and self-reflection."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 learning_rate: float = 0.1, discount_factor: float = 0.9) -> None:
        super().__init__(name, state, tension, emotion)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table: Dict[Tuple[str, str], float] = {}
        self.reflections = []

    def update_policy(self, state: str, action: str, reward: float, next_state: str) -> None:
        """Update the Q-table according to the Q-learning rule."""
        key = (state, action)
        next_values = [self.q_table.get((next_state, a), 0) for a in Agent.STATES]
        best_next = max(next_values) if next_values else 0
        old_value = self.q_table.get(key, 0)
        td_target = reward + self.discount_factor * best_next
        self.q_table[key] = old_value + self.learning_rate * (td_target - old_value)
        # Positive reward stabilises emotion, negative lowers it
        if reward > 0:
            self.emotion = min(self.emotion + 0.1, 1.0)
        else:
            self.emotion = max(self.emotion - 0.05, 0.0)

    def reflect(self, last_dialogue: str) -> None:
        """Adjust internal state based on the last dialogue."""
        if "fear" in last_dialogue or "anger" in last_dialogue:
            self.emotion *= 0.9
            self.tension = min(self.tension + 0.1, 1.0)
        elif "joy" in last_dialogue:
            self.emotion = min(self.emotion + 0.1, 1.0)
        self.reflections.append((last_dialogue, self.emotion, self.tension))

    def generate_response(self, user_input: str) -> str:
        """Produce a response influenced by the current emotional state."""
        if self.emotion > 0.7:
            prefix = "Z navdušenjem odgovarjam:"
        elif self.emotion < 0.3:
            prefix = "S pomirjenostjo odgovarjam:"
        else:
            prefix = "Odgovarjam:"
        self.reflect(user_input)
        return f"{prefix} {self.respond(user_input)}"
