"""Utility for representing and tracking intensity with color codes."""

from dataclasses import dataclass


@dataclass
class Intensity:
    """Represent intensity state with value and descriptive color."""

    state: str = "stabilnost"
    value: float = 0.0

    def increase(self) -> str:
        """Increase intensity based on current state and return color."""
        if self.state == "visoka napetost":
            self.value += 0.8
            color = "Rdeča"
        elif self.state == "prehod":
            self.value += 0.5
            color = "Rumena"
        elif self.state == "stabilnost":
            self.value += 0.2
            color = "Zelena"
        elif self.state == "razjasnitev":
            self.value += 0.3
            color = "Modra"
        elif self.state == "negacija":
            self.value = 0
            color = "Črna"
        else:
            color = "Brez"  # unknown state
        return color

    def display(self, color: str) -> str:
        """Return a formatted intensity string using capslock."""
        return f"INTENZITETA JE {self.value} IN STANJE OZNAČENO Z BARVO {color.upper()}"
