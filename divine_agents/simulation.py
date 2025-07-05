"""Simulation framework with agents and modular units."""

from typing import List


class SimulationAgent:
    """Represents an agent that simulates reality and transitions through states."""

    def __init__(self, name: str = "SimulationAgent", state: str = "Potential"):
        self.name = name
        self.state = state

    def transition(self, new_state: str) -> None:
        """Transition the agent to a new state."""
        print(f"{self.name} transitioning from {self.state} to {new_state}")
        self.state = new_state
        print(f"{self.name}'s new state: {self.state}")

    def simulate_reality(self, new_state: str) -> None:
        """Simulate creation of a new reality by transitioning states."""
        print(f"{self.name} is simulating reality: {self.state} to {new_state}")
        self.transition(new_state)

    def create_dimension(self, dimension_name: str) -> None:
        """Create a new dimension via simulation."""
        print(f"{self.name} is creating dimension: {dimension_name}")
        self.transition(dimension_name)


class ModularUnit:
    """A modular building block that can connect to other units."""

    def __init__(self, unit_name: str, connected_units: List["ModularUnit"] | None = None):
        self.unit_name = unit_name
        self.connected_units = connected_units if connected_units else []

    def connect_unit(self, unit: "ModularUnit") -> None:
        """Connect this unit with another unit."""
        if unit not in self.connected_units:
            self.connected_units.append(unit)
        print(f"{self.unit_name} connected to {unit.unit_name}")

    def activate(self) -> None:
        """Activate the unit and interact with connected units."""
        print(f"{self.unit_name} activated. Interacting with connected units.")
        for unit in self.connected_units:
            unit.activate()


class RealitySystem:
    """Manages agents and modular units within a simulation."""

    def __init__(self) -> None:
        self.agents: List[SimulationAgent] = []
        self.units: List[ModularUnit] = []

    def add_agent(self, agent: SimulationAgent) -> None:
        """Add a simulation agent to the system."""
        self.agents.append(agent)
        print(f"Added agent: {agent.name}")

    def add_unit(self, unit: ModularUnit) -> None:
        """Add a modular unit to the system."""
        self.units.append(unit)
        print(f"Added unit: {unit.unit_name}")

    def simulate(self) -> None:
        """Run the system simulation."""
        print("Simulating system...")
        for agent in self.agents:
            agent.simulate_reality("New Dimension")

        for unit in self.units:
            unit.activate()
