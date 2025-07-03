from typing import Iterable, Optional

from .agent import Agent


class OppositeSeekingAgent(Agent):
    """Agent that always seeks or generates an opposite symbol."""

    def __init__(self, name: str, symbol: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, opposite_symbol: Optional[str] = None) -> None:
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.symbol = symbol
        self.opposite_symbol = opposite_symbol

    def find_or_generate_opposite(self, available_symbols: Optional[Iterable[str]] = None) -> str:
        """Find an opposite symbol in the environment or generate one."""
        if available_symbols:
            for sym in available_symbols:
                if sym != self.symbol:
                    self.opposite_symbol = sym
                    break
        if not self.opposite_symbol:
            self.opposite_symbol = f"\u00ac{self.symbol}"
        return self.opposite_symbol

    def transition(self, available_symbols: Optional[Iterable[str]] = None) -> str:
        """Seek or generate an opposite before performing a state transition."""
        self.find_or_generate_opposite(available_symbols)
        return super().transition()
