"""Module providing an agent that constantly seeks or generates opposition."""

from .agent import Agent
from typing import Iterable, Optional


class OppositeAgent(Agent):
    """Agent that ensures an opposing symbol exists for its identity."""

    def __init__(self, name: str, symbol: str, state: str = "Ego", *, tension: float = 0.0, emotion: float = 0.0, opposite_symbol: Optional[str] = None) -> None:
        super().__init__(name, state, tension, emotion)
        self.symbol = symbol
        self.opposite_symbol = opposite_symbol or self._generate_opposite_symbol()

    def _generate_opposite_symbol(self) -> str:
        """Create an opposite symbol using logical negation notation."""
        return f"\u00ac{self.symbol}"  # prefix with logical NOT

    def seek_opposite(self, environment: Optional[Iterable[str]] = None) -> str:
        """Return an existing or newly generated opposite symbol."""
        if environment and self.opposite_symbol in environment:
            return self.opposite_symbol
        self.opposite_symbol = self._generate_opposite_symbol()
        return self.opposite_symbol

