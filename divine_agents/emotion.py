from dataclasses import dataclass
import numpy as np

@dataclass
class Emotion:
    joy: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    sadness: float = 0.0
    guilt: float = 0.0
    hope: float = 0.0
    pride: float = 0.0
    despair: float = 0.0

    def modulate(self, matrix: np.ndarray) -> np.ndarray:
        """Apply emotional values to modulate a matrix."""
        factor = self.joy - self.anger + self.hope - self.despair
        return matrix * (1 + factor)
