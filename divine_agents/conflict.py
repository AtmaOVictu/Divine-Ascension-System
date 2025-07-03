from typing import List
from .agent import Agent


class OntologicalConflict:
    """Manage conflict-driven transitions between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent):
        self.agent1 = agent1
        self.agent2 = agent2
        self.conflict_level = 0.0

    def increase_conflict(self, value: float = 0.1) -> None:
        """Increase conflict level and escalate tension in both agents."""
        self.conflict_level += value
        self.agent1.update_tension(self.agent1.tension + value)
        self.agent2.update_tension(self.agent2.tension + value)

    def step(self) -> List[str]:
        """Perform one step of the conflict simulation."""
        lines = []
        self.increase_conflict()
        lines.append(f"Konflikt stopnja: {self.conflict_level:.2f}")
        lines.append(f"{self.agent1.name}: {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name}: {self.agent2.respond('Kaj je resnica?')}")
        if self.conflict_level > 0.5:
            self.agent1.state = 'Nasprotje'
            self.agent2.state = 'Nasprotje'
            lines.append('Sistem je v stanju nasprotja.')
        else:
            self.agent1.transition()
            self.agent2.transition()
        return lines
