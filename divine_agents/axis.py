from __future__ import annotations

from dataclasses import dataclass

from .agent import Agent


@dataclass
class DrugaPravaOs:
    """Represents a secondary axis guiding agent direction."""

    name: str
    oscillation: float
    direction: str = "nevtralna"

    def doloci_smer(self, agent: Agent) -> str:
        """Determine direction based on oscillation."""
        if self.oscillation > 0.5:
            self.direction = "proaktivna"
        else:
            self.direction = "defenzivna"
        return self.direction
