from __future__ import annotations

from typing import List

from .agent import Agent


class SimulationAgent(Agent):
    """Agent that can simulate reality and create new dimensions."""

    def simulate_reality(self, new_state: str) -> str:
        """Simulate reality by transitioning to ``new_state``."""
        self.update_emotion(0.6)
        self.state = new_state
        self.history.append(self.state)
        return self.state

    def create_dimension(self, dimension_name: str) -> str:
        """Alias for ``simulate_reality`` to create a dimension."""
        return self.simulate_reality(dimension_name)


class ModularUnit:
    """Building block that can connect to other modular units."""

    def __init__(self, unit_name: str, connected_units: List["ModularUnit"] | None = None):
        self.unit_name = unit_name
        self.connected_units = connected_units if connected_units else []

    def connect_unit(self, unit: "ModularUnit") -> None:
        """Connect this unit with another."""
        if unit not in self.connected_units:
            self.connected_units.append(unit)

    def activate(self) -> List[str]:
        """Activate this unit and recursively activate connected units."""
        lines = [f"{self.unit_name} activated. Interacting with connected units."]
        for unit in self.connected_units:
            lines.extend(unit.activate())
        return lines


class RealitySystem:
    """System that manages agents and modular units."""

    def __init__(self) -> None:
        self.agents: List[SimulationAgent] = []
        self.units: List[ModularUnit] = []

    def add_agent(self, agent: SimulationAgent) -> None:
        self.agents.append(agent)

    def add_unit(self, unit: ModularUnit) -> None:
        self.units.append(unit)

    def simulate(self) -> List[str]:
        """Run the simulation and return log lines."""
        lines = ["Simulating system..."]
        for agent in self.agents:
            agent.simulate_reality("New Dimension")
            lines.append(f"{agent.name}'s new state: {agent.state}")
        for unit in self.units:
            lines.extend(unit.activate())
        return lines
