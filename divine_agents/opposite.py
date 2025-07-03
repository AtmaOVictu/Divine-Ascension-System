from typing import Dict

from .agent import Agent

class OppositeSeekingAgent(Agent):
    """Agent that always seeks or generates opposites for given inputs."""

    def __init__(self, name: str, symbol: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, known_opposites: Dict[str, str] | None = None):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.symbol = symbol
        self.known_opposites = known_opposites or {}

    def find_opposite(self, target: str) -> str:
        """Return opposite for target, generating it if necessary."""
        if target not in self.known_opposites:
            self.known_opposites[target] = f"\xac{target}"
        return self.known_opposites[target]

    def respond_with_opposite(self, statement: str) -> str:
        """Provide the opposite of the statement."""
        opposite = self.find_opposite(statement)
        return f"Nasprotje za '{statement}' je '{opposite}'."
