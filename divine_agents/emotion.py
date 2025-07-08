from dataclasses import dataclass
from typing import List

@dataclass
class Emotion:
    """Container for agent emotions."""
    joy: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    sadness: float = 0.0
    guilt: float = 0.0
    hope: float = 0.0
    pride: float = 0.0
    despair: float = 0.0

    def modulate(self, matrix: List[List[float]]) -> List[List[float]]:
        """Modulate a state matrix based on emotions."""
        influence = (
            self.joy - self.anger + self.hope - self.fear - self.sadness - self.despair
        )
        return [[value * (1 + influence) for value in row] for row in matrix]
