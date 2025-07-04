import random
from typing import List


class SpeculativeAgent:
    """Explore uncertain future possibilities with higher variability."""

    def __init__(self) -> None:
        self.possibilities: List[str] = []

    def speculate(self, current_state: str) -> str:
        """Create a speculative future state with larger random shifts."""
        speculative_state = []
        for char in current_state:
            if char.isalpha():
                speculative_state.append(
                    chr(ord(char) + random.randint(-5, 5))
                )
            else:
                speculative_state.append(char)
        result = "".join(speculative_state)
        self.possibilities.append(result)
        return result
