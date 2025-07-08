from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents a set of emotional states."""

    joy: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    sadness: float = 0.0
    guilt: float = 0.0
    hope: float = 0.0
    pride: float = 0.0
    despair: float = 0.0

    def intensity(self) -> float:
        """Return the dominant emotional intensity."""
        values = [self.joy, self.anger, self.fear, self.sadness,
                  self.guilt, self.hope, self.pride, self.despair]
        return max(abs(v) for v in values)

    def modulate(self, state_value: float) -> float:
        """Modulate a numeric state value using emotional weights."""
        emotional_value = (
            self.joy * 0.3 + self.anger * 0.2 - self.fear * 0.1 -
            self.sadness * 0.15 - self.guilt * 0.2 + self.hope * 0.25 +
            self.pride * 0.1 - self.despair * 0.3
        )
        return state_value * (1 + emotional_value)
