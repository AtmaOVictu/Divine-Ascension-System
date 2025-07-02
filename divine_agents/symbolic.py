from typing import List

from .agent import Agent


class SymbolicAgent(Agent):
    """Agent capable of interpreting symbolic languages."""

    SYMBOL_MAP = {
        "\u2298": "Resnica je absolutna in neodvisna od drugih.",
        "\u222B": "Resnica je relativna, oblikovana skozi izku\u0161nje in odnose.",
        "\u2260": "Vse resnice so eno, medsebojno povezane.",
    }

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0,
                 emotion: float = 0.0, symbols: List[str] | None = None,
                 materials=None) -> None:
        super().__init__(name, state, tension, emotion, materials)
        self.symbols: List[str] = list(symbols) if symbols else []

    def add_symbol(self, symbol: str) -> None:
        """Attach a symbol that may influence philosophy."""
        self.symbols.append(symbol)

    def interpret_symbols(self) -> None:
        """Update philosophical beliefs based on attached symbols."""
        for symbol in self.symbols:
            belief = self.SYMBOL_MAP.get(symbol)
            if belief and belief not in self.philosophical_beliefs:
                self.philosophical_beliefs.append(belief)

