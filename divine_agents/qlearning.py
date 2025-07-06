import random


class QLearningAgent:
    """Extend Agent with simple Q-learning capability."""
    def __init__(self, actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.actions = actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = {}

    def get_action(self, state):
        if random.uniform(0, 1) < self.epsilon or state not in self.q_table:
            return random.choice(self.actions)
        return max(self.q_table[state], key=self.q_table[state].get)

    def update_q_value(self, state, action, reward, next_state):
        self.q_table.setdefault(state, {})
        self.q_table.setdefault(next_state, {})
        max_q_value = max(self.q_table[next_state].values(), default=0)
        current_q_value = self.q_table[state].get(action, 0)
        new_value = current_q_value + self.learning_rate * (
            reward + self.discount_factor * max_q_value - current_q_value
        )
        self.q_table[state][action] = new_value
        return new_value
