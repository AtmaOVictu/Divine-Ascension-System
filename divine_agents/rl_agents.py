from __future__ import annotations

from typing import Dict

from .agent import Agent


class RLAgent(Agent):
    """Agent with a simple Q-learning mechanism."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 learning_rate: float = 0.1, discount_factor: float = 0.9) -> None:
        super().__init__(name, state, tension, emotion)
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.q_table: Dict[str, Dict[str, float]] = {}

    def choose_action(self, state: str) -> str:
        """Select the best known action for a state."""
        actions = self.q_table.get(state, {})
        if not actions:
            return "respond"
        return max(actions, key=actions.get)

    def update_policy(self, state: str, action: str, reward: float, next_state: str) -> None:
        """Update the Q-table based on received reward."""
        self.q_table.setdefault(state, {})
        self.q_table.setdefault(next_state, {})
        best_next = max(self.q_table[next_state], default=0)
        current = self.q_table[state].get(action, 0.0)
        td_target = reward + self.discount_factor * best_next
        td_error = td_target - current
        self.q_table[state][action] = current + self.learning_rate * td_error


class ReflectiveAgent(RLAgent):
    """Agent capable of self-reflection influencing emotions and tension."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0,
                 learning_rate: float = 0.1, discount_factor: float = 0.9) -> None:
        super().__init__(name, state, tension, emotion, learning_rate, discount_factor)
        self.reflections = []

    def reflect(self, last_dialogue: str) -> None:
        """Adjust emotion and tension based on the last dialogue."""
        if "fear" in last_dialogue or "anger" in last_dialogue:
            self.emotion = max(self.emotion * 0.9, 0.0)
            self.tension += 0.1
        elif "joy" in last_dialogue:
            self.emotion = min(self.emotion + 0.1, 1.0)
        self.reflections.append((last_dialogue, self.emotion, self.tension))

    def generate_response(self, question: str) -> str:
        """Produce a philosophical answer influenced by current emotion."""
        base = self.respond(question)
        if self.emotion > 0.7:
            prefix = "Z navdušenjem povem, "
        elif self.emotion < 0.3:
            prefix = "Mirno povem, "
        else:
            prefix = ""
        return prefix + base


def reinforced_dialogue(agent1: ReflectiveAgent, agent2: ReflectiveAgent) -> list[str]:
    """Generate a short dialogue where agents may transition state."""
    conversation = []

    # Initial statements
    conversation.append(f"{agent1.name} ({agent1.state}): {agent1.generate_response('Kaj je resnica?')}")
    conversation.append(f"{agent2.name} ({agent2.state}): {agent2.generate_response('Kaj je resnica?')}")

    # Update emotions to trigger possible transitions
    agent1.update_emotion(agent1.emotion + 0.6)
    agent1.reflect('fear')
    conversation.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent2.emotion + 0.6)
    agent2.reflect('joy')
    conversation.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    conversation.append(f"{agent1.name}: {agent1.generate_response('Kaj je resnica?')}")
    conversation.append(f"{agent2.name}: {agent2.generate_response('Kaj je resnica?')}")

    return conversation
