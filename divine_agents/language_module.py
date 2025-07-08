from __future__ import annotations

from typing import Optional
from .agent import Agent


class LanguageModule:
    """Process input and generate responses influenced by an agent's state."""

    def __init__(self, agent: Agent):
        self.agent = agent

    def process_input(self, text: str) -> None:
        """Adjust agent emotion if emotional keywords are present."""
        if "anger" in text or "jeza" in text:
            self.agent.update_emotion(0.6)
        elif "fear" in text or "strah" in text:
            self.agent.update_emotion(0.7)
        elif "joy" in text or "veselje" in text:
            self.agent.update_emotion(0.3)

    def generate_response(self) -> str:
        """Generate a philosophical response based on the agent's state."""
        if self.agent.state == "Ego":
            return "Resnica je absolutna in neodvisna od drugih."
        if self.agent.state == "Jaz":
            return "Resnica je relativna, oblikovana z nasimi odnosi."
        return "Vse resnice so eno, medsebojno povezane."
