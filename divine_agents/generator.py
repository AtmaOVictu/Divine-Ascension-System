"""Ontological generator responsible for energizing agents."""
from .agent import Agent

class Generator:
    """Generator acts as a catalyst for agent transitions."""

    def __init__(self, power: float = 1.0, active: bool = False):
        self.power = power
        self.active = active

    def activate(self, power: float | None = None) -> None:
        """Activate the generator with optional power level."""
        self.active = True
        if power is not None:
            self.power = power

    def stimulate(self, agent: Agent, emotion_boost: float = 0.5) -> str:
        """Increase agent emotion and attempt a state transition."""
        if not self.active:
            return agent.state
        agent.update_emotion(agent.emotion + emotion_boost * self.power)
        return agent.transition()
