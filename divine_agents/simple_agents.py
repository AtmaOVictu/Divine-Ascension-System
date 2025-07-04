"""Simple agents representing bits or alphabet symbols."""
from dataclasses import dataclass

@dataclass
class BitAgent:
    """Agent that toggles between bit values 0 and 1."""
    id: str
    value: int
    note: str = ""

    def transition(self) -> int:
        """Toggle the bit value."""
        self.value = 1 if self.value == 0 else 0
        return self.value

@dataclass
class AlphabetAgent:
    """Agent that cycles through alphabet symbols."""
    id: str
    symbol: str
    note: str = ""
    _alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def transition(self) -> str:
        """Move to the next symbol in the alphabet."""
        index = self._alphabet.index(self.symbol)
        next_index = (index + 1) % len(self._alphabet)
        self.symbol = self._alphabet[next_index]
        return self.symbol
