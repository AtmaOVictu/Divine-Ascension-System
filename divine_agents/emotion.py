from dataclasses import dataclass

@dataclass
class Emotion:
    """Represents an emotion influencing agent state."""
    name: str
    weight: float
    pressure: float
    potency: float
    definitive_share: float

    @property
    def force(self) -> float:
        """Compute overall emotional force."""
        return self.weight + self.pressure + self.potency + self.definitive_share
