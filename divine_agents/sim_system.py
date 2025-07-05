from typing import List
from .agent import Agent


class SimulationAgent(Agent):
    """Agent capable of simulating reality and creating dimensions."""

    def simulate_reality(self, emotion_increase: float = 0.0, tension_increase: float = 0.0) -> str:
        """Increase emotion or tension and attempt a state transition."""
        if emotion_increase:
            new_emotion = min(1.0, self.emotion + emotion_increase)
            self.update_emotion(new_emotion)
        if tension_increase:
            self.update_tension(self.tension + tension_increase)
        return self.transition()

    def create_dimension(self, dimension_name: str) -> str:
        """Placeholder for creating a new dimension through simulation."""
        return self.simulate_reality(emotion_increase=0.6)


class ModularUnit:
    """Building block that can be connected with other units."""

    def __init__(self, unit_name: str):
        self.unit_name = unit_name
        self.connected_units: List["ModularUnit"] = []

    def connect_unit(self, unit: "ModularUnit") -> None:
        if unit not in self.connected_units:
            self.connected_units.append(unit)

    def activate(self) -> List[str]:
        lines = [f"{self.unit_name} activated."]
        for unit in self.connected_units:
            lines.extend(unit.activate())
        return lines


class RealitySystem:
    """System managing simulation agents and modular units."""

    def __init__(self) -> None:
        self.agents: List[SimulationAgent] = []
        self.units: List[ModularUnit] = []

    def add_agent(self, agent: SimulationAgent) -> None:
        self.agents.append(agent)

    def add_unit(self, unit: ModularUnit) -> None:
        self.units.append(unit)

    def simulate(self) -> List[str]:
        lines: List[str] = []
        for agent in self.agents:
            lines.append(f"{agent.name} state: {agent.state}")
            lines.append(f"{agent.name} transitions to {agent.simulate_reality(emotion_increase=0.8)}")
        for unit in self.units:
            lines.extend(unit.activate())
        return lines
