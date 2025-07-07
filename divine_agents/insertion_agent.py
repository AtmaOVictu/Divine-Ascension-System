from typing import Any, Callable

from .agent import Agent


class InsertionAgent:
    """Add states, behaviors, or knowledge to an existing :class:`Agent`."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def add_state(self, state: str) -> None:
        """Add a new state to the agent if it does not already exist."""
        if state not in self.agent.STATES:
            self.agent.STATES += (state,)

    def add_behavior(self, name: str, func: Callable) -> None:
        """Attach a new behavior (method) to the agent."""
        bound = func.__get__(self.agent, self.agent.__class__)
        setattr(self.agent, name, bound)

    def add_knowledge(self, key: str, value: Any) -> None:
        """Store new knowledge on the agent."""
        if not hasattr(self.agent, "knowledge"):
            self.agent.knowledge = {}
        self.agent.knowledge[key] = value
