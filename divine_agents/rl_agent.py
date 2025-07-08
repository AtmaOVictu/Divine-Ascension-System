"""Reinforcement learning enabled agent."""

from .agent import Agent


class RLAgent(Agent):
    """Agent with basic reinforcement learning and introspection capabilities."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, learning_rate: float = 0.1,
                 discount_factor: float = 0.9) -> None:
        super().__init__(name, state, tension, emotion)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table: dict[str, dict[str, float]] = {}

    def update_policy(self, state: str, action: str, reward: float,
                      next_state: str) -> None:
        """Update policy using a simple Q-learning rule."""
        self.q_table.setdefault(state, {})
        self.q_table.setdefault(next_state, {})
        current = self.q_table[state].get(action, 0.0)
        best_next = max(self.q_table[next_state].values(), default=0.0)
        td_target = reward + self.discount_factor * best_next
        td_error = td_target - current
        self.q_table[state][action] = current + self.learning_rate * td_error

    def reflect(self, last_dialogue: str) -> None:
        """Adjust emotional state based on previous dialogue."""
        if any(word in last_dialogue.lower() for word in ("fear", "anger", "strah", "jeza")):
            self.emotion = max(self.emotion - 0.1, 0.0)
            self.tension += 0.1
        elif any(word in last_dialogue.lower() for word in ("joy", "veselje")):
            self.emotion = min(self.emotion + 0.1, 1.0)
        self.history.append(("reflection", self.emotion, self.tension))

    def generate_response(self, user_input: str) -> str:
        """Generate a response influenced by emotion and ontological state."""
        base = self.respond(user_input)
        if self.emotion > 0.7:
            return f"{base} Čutim močno veselje."
        if self.emotion < 0.3:
            return f"{base} Ostajam umirjen."
        return base
