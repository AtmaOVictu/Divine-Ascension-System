class BitAgent:
    """Simple agent representing a single bit."""

    def __init__(self, agent_id: str, value: int, note: str = ""):
        self.id = agent_id
        self.value = value
        self.note = note

    def transition(self) -> int:
        """Flip the bit from 0 to 1 or 1 to 0."""
        self.value = 1 if self.value == 0 else 0
        return self.value


class AlphabetAgent:
    """Agent that cycles through the alphabet."""

    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self, agent_id: str, symbol: str, note: str = ""):
        self.id = agent_id
        self.symbol = symbol
        self.note = note

    def transition(self) -> str:
        """Move to the next symbol in the alphabet."""
        index = self.ALPHABET.index(self.symbol)
        self.symbol = self.ALPHABET[(index + 1) % len(self.ALPHABET)]
        return self.symbol
