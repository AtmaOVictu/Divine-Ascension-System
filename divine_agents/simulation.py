from typing import List, Optional
from .agent import Agent


class SimulationAgent(Agent):
    """Agent capable of simulating transitions to new dimensions."""

    def transition_to(self, new_state: str) -> str:
        """Transition to a new state ignoring thresholds."""
        self.state = new_state
        self.history.append(self.state)
        return self.state

    def simulate_reality(self, new_state: str) -> str:
        """Simulate the creation of a new reality by transitioning state."""
        return self.transition_to(new_state)

    def create_dimension(self, dimension_name: str) -> str:
        """Create a new dimension in the simulation."""
        return self.transition_to(dimension_name)


class ModularUnit:
    """A modular unit that can connect to other units."""

    def __init__(self, unit_name: str, connected_units: Optional[List['ModularUnit']] = None):
        self.unit_name = unit_name
        self.connected_units: List['ModularUnit'] = connected_units if connected_units else []

    def connect_unit(self, unit: 'ModularUnit') -> None:
        if unit not in self.connected_units:
            self.connected_units.append(unit)

    def activate(self) -> None:
        for unit in self.connected_units:
            unit.activate()


class RealitySystem:
    """System managing agents and modular units."""

    def __init__(self) -> None:
        self.agents: List[SimulationAgent] = []
        self.units: List[ModularUnit] = []

    def add_agent(self, agent: SimulationAgent) -> None:
        self.agents.append(agent)

    def add_unit(self, unit: ModularUnit) -> None:
        self.units.append(unit)

    def simulate(self) -> None:
        for agent in self.agents:
            agent.simulate_reality("New Dimension")
        for unit in self.units:
            unit.activate()
