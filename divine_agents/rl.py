from typing import Dict, Tuple


class ReinforcementLearner:
    """A simple reinforcement learner that stores rewards per state-action."""

    def __init__(self):
        self.q_table: Dict[Tuple[str, str], float] = {}

    def choose_action(self, state: str, actions) -> str:
        """Choose the best action based on current Q-values."""
        best_value = float('-inf')
        best_action = actions[0]
        for action in actions:
            value = self.q_table.get((state, action), 0.0)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action

    def update(self, state: str, action: str, reward: float) -> None:
        """Update Q-value for given state-action pair."""
        key = (state, action)
        self.q_table[key] = self.q_table.get(key, 0.0) + reward
