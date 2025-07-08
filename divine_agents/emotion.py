from dataclasses import dataclass
import numpy as np

@dataclass
class Emotion:
    """Represents an agent's emotional state."""

    joy: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    sadness: float = 0.0
    guilt: float = 0.0
    hope: float = 0.0
    pride: float = 0.0
    despair: float = 0.0
    regret: float = 0.0
    compassion: float = 0.0
    envy: float = 0.0
    trust: float = 0.0

    def transition(self) -> None:
        """Handle corrective emotional transitions."""
        if self.despair > 0.8:
            self.hope = min(1.0, self.hope + 0.4)
            self.despair = max(0.0, self.despair - 0.2)
        elif self.regret > 0.8:
            self.hope = min(1.0, self.hope + 0.2)
            self.regret = max(0.0, self.regret - 0.2)
        elif self.sadness > 0.8:
            self.compassion = min(1.0, self.compassion + 0.3)
            self.sadness = max(0.0, self.sadness - 0.2)

    def modulate(self, matrix):
        """Modulate agent state based on current emotions."""
        factor = 1 + self.joy - self.sadness
        return [[cell * factor for cell in row] for row in matrix]
