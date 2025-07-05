"""Ontological generator to trigger state transitions."""

from .agent import Agent


class Generator:
    """Generator that amplifies an agent's tension to enable transitions."""

    def __init__(self, active: bool = False, energy: float = 0.0) -> None:
        self.active = active
        self.energy = energy

    def activate(self, energy: float = 1.0) -> None:
        """Activate the generator with a given energy level."""
        self.active = True
        self.energy = energy

    def deactivate(self) -> None:
        """Deactivate the generator."""
        self.active = False
        self.energy = 0.0

    def energize(self, agent: Agent) -> str:
        """Apply energy to an agent and possibly trigger a state transition."""
        if not self.active:
            return agent.state

        agent.update_tension(agent.tension + self.energy)
        return agent.transition()
