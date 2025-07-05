"""Simulation utilities for ontological agents in imaginary time cycles."""

from typing import List, Tuple

from .agent import Agent


class ImaginaryTimeSimulation:
    """Run agents through imaginary time cycles updating emotion and tension."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent
        self.value = 0.0
        self.history: List[Tuple[int, str, float]] = []
        self.loop_count = 0

    def step(self) -> str:
        """Advance one cycle, adjusting values and returning the new state."""
        self.loop_count += 1
        self.value = min(1.0, self.value + 0.1)
        # Use value as emotion intensity
        self.agent.update_emotion(self.value)
        state = self.agent.transition()
        self.history.append((self.loop_count, state, self.value))
        return state

    def run(self, cycles: int = 10) -> List[Tuple[int, str, float]]:
        """Run the simulation for the given number of cycles."""
        for _ in range(cycles):
            self.step()
        return self.history
