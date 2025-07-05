# -*- coding: utf-8 -*-
"""Ontological processors for managing agent transitions."""
from __future__ import annotations

from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:  # pragma: no cover - used for type hints only
    from .agent import Agent


class MetaEgo:
    """Simple meta-level ego stabilizer."""

    def usklajuj(self) -> None:
        """Placeholder for ego harmonization."""
        # In a full implementation this could adjust internal states
        pass


class MetaJaz:
    """Simple meta-level jaz stabilizer."""

    def stabiliziraj(self) -> None:
        """Placeholder for jaz stabilization."""
        pass


class Bog:
    """Represents the universal laws guiding agents."""

    def uravnavaj(self, agent: "Agent") -> None:
        """Placeholder for universal regulation."""
        # Potentially reduce tension to keep harmony
        agent.tension = max(0.0, agent.tension - 0.1)


class OntoProcesor:
    """Central processor coordinating agent transitions."""

    def __init__(self, agent: "Agent", meta_ego: Optional[MetaEgo] = None,
                 meta_jaz: Optional[MetaJaz] = None, bog: Optional[Bog] = None) -> None:
        self.agent = agent
        self.meta_ego = meta_ego or MetaEgo()
        self.meta_jaz = meta_jaz or MetaJaz()
        self.bog = bog or Bog()

    def izracunaj_napetost(self) -> None:
        """Check tension and harmonize if high."""
        if self.agent.tension > 0.7:
            self.meta_ego.usklajuj()

    def analizira_prehod(self, simbol: str) -> str:
        """Analyze transition symbol and update agent state."""
        if simbol == "A":
            self.agent.update_tension(0.8)
        elif simbol == "B":
            self.agent.update_emotion(0.6)
        elif simbol == "C":
            self.agent.update_tension(0.0)
        new_state = self.agent.transition()
        self.meta_jaz.stabiliziraj()
        self.meta_ego.usklajuj()
        self.bog.uravnavaj(self.agent)
        return new_state

    def optimiziraj_prehod(self) -> None:
        """Simplified optimization step."""
        if self.agent.state == "Ego" and self.agent.tension > 0.7:
            self.agent.transition()
        elif self.agent.state == "Jaz" and self.agent.tension > 0.7:
            self.agent.transition()

    def preveri_stanje(self) -> str:
        """Return textual description of the agent state."""
        return self.agent.state
