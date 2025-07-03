"""Ontological transition tracking for agents."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Tuple


@dataclass
class Ontoznano:
    """Represents the agent's progress through ontological phases."""

    podrocje: str = "neznano"
    napredek: int = 0
    historia: List[Tuple[str, int]] = field(default_factory=list)

    def prehod_v_ontoznano(self, prehod: str) -> None:
        """Change phase depending on the provided transition keyword."""
        if prehod == "samospoznanje":
            self.podrocje = "poznavanje lastne resnice"
            self.napredek = 100
        elif prehod == "logični prehod":
            self.podrocje = "logična analiza"
            self.napredek = 50
        elif prehod == "emotivni prehod":
            self.podrocje = "emocionalna refleksija"
            self.napredek = 75
        else:
            self.podrocje = "neznano"
            self.napredek = 0

        self.historia.append((prehod, self.napredek))
        self.prikazi_napredek()

    def prikazi_napredek(self) -> None:
        """Display current progress in a simple textual form."""
        bar = "#" * (self.napredek // 10)
        print(f"Napredek [{self.podrocje}]: {bar} {self.napredek}%")
