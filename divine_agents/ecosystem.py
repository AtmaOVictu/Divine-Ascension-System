import random
from typing import List, Tuple
from .agent import Agent


class Ecosystem:
    """Simulate an ecosystem of agents influenced by capacitors."""

    def __init__(self, agents: List[Agent]):
        self.agents = agents
        self.capacitators = [random.uniform(0.5, 1.5) for _ in agents]
        self.energy = [random.uniform(0.1, 0.9) for _ in agents]
        self.voltage = [random.uniform(0.2, 1.0) for _ in agents]
        self.energy_log: List[List[float]] = []
        self.voltage_log: List[List[float]] = []

    def step(self) -> None:
        """Perform a single time step, updating energy, voltage and agent states."""
        energy_change = [random.gauss(0, 1) * c for c in self.capacitators]
        voltage_change = [random.gauss(0, 1) * c for c in self.capacitators]

        self.energy = [min(max(e + de, 0.0), 1.0) for e, de in zip(self.energy, energy_change)]
        self.voltage = [min(max(v + dv, 0.0), 1.0) for v, dv in zip(self.voltage, voltage_change)]

        self.energy_log.append(self.energy.copy())
        self.voltage_log.append(self.voltage.copy())

        for idx, agent in enumerate(self.agents):
            agent.update_emotion(self.energy[idx])
            agent.update_tension(self.voltage[idx])
            agent.transition()

    def run(self, steps: int = 100) -> Tuple[List[List[float]], List[List[float]]]:
        """Run the simulation for the given number of steps."""
        for _ in range(steps):
            self.step()
        return self.energy_log, self.voltage_log
