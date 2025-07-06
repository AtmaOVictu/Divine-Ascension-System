from __future__ import annotations

from dataclasses import dataclass
from typing import List
import random

from .agent import Agent


@dataclass
class EcosystemRecord:
    step: int
    states: List[str]
    tensions: List[float]
    emotions: List[float]


class Ecosystem:
    """Simulate an ecosystem of agents influenced by capacitors."""

    def __init__(self, agent_names: List[str]):
        self.agents = [Agent(name) for name in agent_names]
        self.capacitors = [random.uniform(0.5, 1.5) for _ in self.agents]
        self.history: List[EcosystemRecord] = []

    def step(self, k: int) -> None:
        for idx, agent in enumerate(self.agents):
            change = random.gauss(0, 1) * self.capacitors[idx]
            new_emotion = min(max(agent.emotion + change, 0), 1)
            agent.update_emotion(new_emotion)
            agent.transition()
        self.history.append(
            EcosystemRecord(
                step=k,
                states=[a.state for a in self.agents],
                tensions=[a.tension for a in self.agents],
                emotions=[a.emotion for a in self.agents],
            )
        )

    def run(self, steps: int = 10) -> List[EcosystemRecord]:
        for k in range(steps):
            self.step(k)
        return self.history
