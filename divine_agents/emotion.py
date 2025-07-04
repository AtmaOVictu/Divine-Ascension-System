"""Emotion handling with Afekt and Efektiv classes."""
from dataclasses import dataclass

@dataclass
class Afekt:
    """Represents a short-lived intense emotional impulse."""
    name: str
    intensity: float

    def transform(self) -> "Efektiv":
        """Transform Afekt into a longer lasting Efektiv."""
        if self.intensity > 0.8:
            return Efektiv(self.name, self.intensity / 2)
        return Efektiv(self.name, self.intensity * 1.2)

@dataclass
class Efektiv:
    """Represents a sustained emotional effect."""
    name: str
    sustained_intensity: float

    def integrate(self) -> str:
        """Return description of integration based on intensity."""
        if self.sustained_intensity > 1:
            return "Stabilnost dosežena"
        return "Nadaljevanje procesa"
