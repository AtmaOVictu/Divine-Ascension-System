class BitAgent:
    """Agent representing a single bit value that toggles between 0 and 1."""

    def __init__(self, id_: str, value: int = 0, note: str = ""):
        self.id = id_
        self.value = value
        self.note = note

    def transition(self) -> int:
        """Toggle the bit value and return the new value."""
        self.value = 1 - self.value
        return self.value


class AlphabetAgent:
    """Agent representing a symbol in the English alphabet."""

    _alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, id_: str, symbol: str = "A", note: str = ""):
        if symbol not in self._alphabet:
            raise ValueError("Invalid symbol")
        self.id = id_
        self.symbol = symbol
        self.note = note

    def transition(self) -> str:
        """Move to the next symbol in the alphabet and return it."""
        idx = self._alphabet.index(self.symbol)
        self.symbol = self._alphabet[(idx + 1) % len(self._alphabet)]
        return self.symbol
