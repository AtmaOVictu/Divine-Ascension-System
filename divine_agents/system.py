from __future__ import annotations

from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue
from .modular_unit import ModularUnit


class RealitySystem:
    """System managing agents and modular units."""

    def __init__(self) -> None:
        self.agents: List[Agent] = []
        self.units: List[ModularUnit] = []

    def add_agent(self, agent: Agent) -> None:
        self.agents.append(agent)

    def add_unit(self, unit: ModularUnit) -> None:
        self.units.append(unit)

    def simulate(self) -> List[str]:
        """Simulate agent dialogues and unit activations."""
        lines: List[str] = []
        if len(self.agents) >= 2:
            lines.extend(philosophical_dialogue(self.agents[0], self.agents[1]))
        for unit in self.units:
            lines.extend(unit.activate())
        return lines
