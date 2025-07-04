from typing import Dict

from .agent import Agent


class EthicalAgent(Agent):
    """Agent extended with ethical beliefs influencing moral choices."""

    def __init__(self, name: str, beliefs: Dict[str, float], emotions: Dict[str, float],
                 state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.beliefs = beliefs
        self.emotions_map = emotions

    def calculate_moral_choice(self) -> str:
        """Return a moral decision based on beliefs and emotions."""
        honesty = self.beliefs.get("honesty", 0.0)
        guilt = self.emotions_map.get("guilt", 0.0)
        if honesty > 0.8 and guilt > 0.5:
            return "Tell the truth"
        return "Lie for self-protection"
