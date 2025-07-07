from .agent import Agent
from typing import Any, Callable

class InsertionAgent:
    """Utility for inserting states, data, and behaviors into an Agent."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def insert_state(self, new_state: str) -> None:
        """Insert a new state into the agent and append to history."""
        if new_state not in Agent.STATES:
            raise ValueError(f"Unknown state: {new_state}")
        self.agent.state = new_state
        self.agent.history.append(new_state)

    def insert_data(self, data: Any) -> None:
        """Attach arbitrary data to the agent."""
        if not hasattr(self.agent, "data"):
            self.agent.data = []  # type: ignore[attr-defined]
        self.agent.data.append(data)  # type: ignore[attr-defined]

    def modify_behavior(self, behavior: Callable[[str], str]) -> None:
        """Replace the agent's respond method with a new behavior."""
        # bind the new behavior to the agent instance
        self.agent.respond = behavior.__get__(self.agent, Agent)
