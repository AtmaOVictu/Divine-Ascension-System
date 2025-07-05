from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - for type hints only
    from .agent import Agent


class MetaEgo:
    """Simple representation of MetaEgo managing tension."""

    def __init__(self) -> None:
        self.napetost = 0.0

    def usklajuj(self) -> None:
        """Reduce tension slightly to simulate synchronization."""
        if self.napetost > 0:
            self.napetost -= 0.1


class MetaJaz:
    """Placeholder for MetaJaz stabilization logic."""

    def stabiliziraj(self) -> None:  # pragma: no cover - simple placeholder
        pass


class Bog:
    """Placeholder for higher-level regulation."""

    def uravnavaj(self, agent: 'Agent') -> None:  # pragma: no cover - simple placeholder
        pass


class OntoProcesor:
    """Central module for processing ontological transitions."""

    def __init__(self, agent: 'Agent', meta_ego: MetaEgo, meta_jaz: MetaJaz, bog: Bog) -> None:
        self.agent = agent
        self.meta_ego = meta_ego
        self.meta_jaz = meta_jaz
        self.bog = bog

    def izracunaj_napetost(self) -> None:
        """Calculate tension and coordinate with MetaEgo."""
        if self.meta_ego.napetost > 0.7:
            self.meta_ego.usklajuj()

    def analizira_prehod(self, simbol: str) -> None:
        """Analyze incoming symbol and trigger actions."""
        if simbol == "A":
            self.agent.update_emotion(0.6)
        elif simbol == "B":
            self.agent.update_tension(0.8)
        elif simbol == "C":
            self.agent.update_tension(0.0)
        elif simbol == "D":
            self.agent.transition()
        elif simbol == "E":
            self.agent.state = "Enotnost"

        self.meta_jaz.stabiliziraj()
        self.meta_ego.usklajuj()
        self.bog.uravnavaj(self.agent)

    def optimiziraj_prehod(self) -> None:
        """Simple optimization to move agent towards higher state."""
        if self.agent.state == "Ego":
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz":
            self.agent.state = "Enotnost"

    def preveri_stanje(self) -> str:
        """Return current agent state for inspection."""
        return self.agent.state
