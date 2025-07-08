from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents complex emotional state for an agent."""
    joy: float = 0.0
    anger: float = 0.0
    fear: float = 0.0
    sadness: float = 0.0
    guilt: float = 0.0
    hope: float = 0.0
    pride: float = 0.0
    despair: float = 0.0

    def as_array(self) -> list[float]:
        return [
            self.joy,
            self.anger,
            self.fear,
            self.sadness,
            self.guilt,
            self.hope,
            self.pride,
            self.despair,
        ]

    def intensity(self) -> float:
        """Return average intensity of all emotions."""
        arr = [abs(x) for x in self.as_array()]
        return sum(arr) / len(arr)

    def modulate(self, matrix: list[list[float]]) -> list[list[float]]:
        """Simple modulation of a matrix by joy and fear."""
        factor = 1 + self.joy - self.fear
        return [[value * factor for value in row] for row in matrix]

