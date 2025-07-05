# coding: utf-8
"""Simulation components for dynamic reality creation."""
from __future__ import annotations

from typing import List


class SimulationAgent:
    """Represents an agent that simulates reality through state transitions."""

    def __init__(self, name: str = "SimulationAgent", state: str = "Potential"):
        self.name = name
        self.state = state

    def transition(self, new_state: str) -> None:
        """Transition the agent to a new state."""
        print(f"{self.name} transitioning from {self.state} to {new_state}")
        self.state = new_state
        print(f"{self.name}'s new state: {self.state}")

    def simulate_reality(self, new_state: str) -> None:
        """Simulate the creation of a new reality by transitioning state."""
        print(f"{self.name} is simulating reality: {self.state} to {new_state}")
        self.transition(new_state)

    def create_dimension(self, dimension_name: str) -> None:
        """Create a new dimension through simulation."""
        print(f"{self.name} is creating dimension: {dimension_name}")
        self.transition(dimension_name)


class ModularUnit:
    """A modular unit that can connect with other units."""

    def __init__(self, unit_name: str, connected_units: List[ModularUnit] | None = None):
        self.unit_name = unit_name
        self.connected_units: List[ModularUnit] = connected_units if connected_units else []

    def connect_unit(self, unit: 'ModularUnit') -> None:
        """Connect this unit with another."""
        if unit not in self.connected_units:
            self.connected_units.append(unit)
        print(f"{self.unit_name} connected to {unit.unit_name}")

    def activate(self) -> None:
        """Activate this unit and its connected units."""
        print(f"{self.unit_name} activated. Interacting with connected units.")
        for unit in self.connected_units:
            unit.activate()


class RealitySystem:
    """System that manages agents and units."""

    def __init__(self) -> None:
        self.agents: List[SimulationAgent] = []
        self.units: List[ModularUnit] = []

    def add_agent(self, agent: SimulationAgent) -> None:
        self.agents.append(agent)
        print(f"Added agent: {agent.name}")

    def add_unit(self, unit: ModularUnit) -> None:
        self.units.append(unit)
        print(f"Added unit: {unit.unit_name}")

    def simulate(self) -> None:
        """Simulate the system's evolution."""
        print("Simulating system...")
        for agent in self.agents:
            agent.simulate_reality("New Dimension")

        for unit in self.units:
            unit.activate()


__all__ = [
    "SimulationAgent",
    "ModularUnit",
    "RealitySystem",
]
