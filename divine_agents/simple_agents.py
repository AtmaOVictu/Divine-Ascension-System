"""Simple agents representing a bit or an alphabet symbol."""

class BitAgent:
    """Agent that toggles between 0 and 1."""

    def __init__(self, agent_id: str, value: int = 0, note: str = "") -> None:
        self.id = agent_id
        self.value = value
        self.note = note

    def transition(self) -> int:
        """Toggle the bit value and return the new value."""
        self.value = 1 if self.value == 0 else 0
        return self.value


class AlphabetAgent:
    """Agent that cycles through the English alphabet."""

    _ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, agent_id: str, symbol: str = "A", note: str = "") -> None:
        if symbol not in self._ALPHABET:
            raise ValueError("Invalid starting symbol")
        self.id = agent_id
        self.symbol = symbol
        self.note = note

    def transition(self) -> str:
        """Move to the next symbol in the alphabet and return it."""
        index = self._ALPHABET.index(self.symbol)
        index = (index + 1) % len(self._ALPHABET)
        self.symbol = self._ALPHABET[index]
        return self.symbol
