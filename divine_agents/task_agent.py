import time
from typing import List
from .agent import Agent


class Krak:
    """Represents a task that may be triggered by agent state or emotion."""

    def __init__(self, name: str, condition: str):
        self.name = name
        self.condition = condition
        self.completed = False
        self.timestamp = None

    def check_condition(self, agent: Agent) -> bool:
        """Return True if the krak should activate for the given agent."""
        if self.condition == "high_emotion":
            return agent.emotion > 0.7
        if self.condition == "state_jaz":
            return agent.state == "Jaz"
        return False

    def activate(self) -> str:
        """Mark the krak as completed and return an activation message."""
        self.completed = True
        self.timestamp = time.time()
        return f"Krak {self.name} activated"


class TaskAgent(Agent):
    """Agent that manages and activates kraks during transitions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.kraks: List[Krak] = []

    def add_krak(self, krak: Krak) -> None:
        """Register a krak with this agent."""
        self.kraks.append(krak)

    def transition(self) -> str:
        """Perform state transition and activate any eligible kraks."""
        new_state = super().transition()
        for krak in self.kraks:
            if not krak.completed and krak.check_condition(self):
                krak.activate()
        return new_state

