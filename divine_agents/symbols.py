"""Symbol management for the divine agents system."""
from typing import Dict, List

class OntologicalSymbol:
    """Represents a symbolic unit with a specific meaning."""

    def __init__(self, symbol: str, meaning: str) -> None:
        self.symbol = symbol
        self.meaning = meaning

    def activate(self) -> str:
        """Return a message indicating activation."""
        return f"Symbol '{self.symbol}' activated with meaning: {self.meaning}"

    def transition(self, new_meaning: str) -> str:
        """Transition the symbol to a new meaning."""
        old_meaning = self.meaning
        self.meaning = new_meaning
        return (
            f"Symbol '{self.symbol}' transitioned from '{old_meaning}' to '{new_meaning}'"
        )


class OntologicalSymbolSet:
    """Manage a collection of ontological symbols."""

    def __init__(self) -> None:
        self.symbols: Dict[str, OntologicalSymbol] = {}

    def add_symbol(self, symbol: OntologicalSymbol) -> None:
        """Add a symbol to the collection."""
        self.symbols[symbol.symbol] = symbol

    def remove_symbol(self, symbol_key: str) -> None:
        """Remove a symbol from the collection by its key."""
        self.symbols.pop(symbol_key, None)

    def activate_all(self) -> List[str]:
        """Activate all symbols and return their activation messages."""
        return [sym.activate() for sym in self.symbols.values()]

    def transition_all(self, transitions: Dict[str, str]) -> List[str]:
        """Transition multiple symbols based on provided mappings."""
        msgs = []
        for key, new_meaning in transitions.items():
            symbol = self.symbols.get(key)
            if symbol:
                msgs.append(symbol.transition(new_meaning))
        return msgs

