from __future__ import annotations

from .agent import Agent


class ReasonAgent(Agent):
    """Agent that uses logical reasoning to interpret context."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, logic_level: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.logic_level = logic_level

    def update_logic(self, value: float) -> None:
        """Update logic level, capped at 1.0."""
        self.logic_level = min(1.0, self.logic_level + value)

    def reason(self, context: str) -> str:
        """Return reasoning output depending on logic level."""
        if self.logic_level > 0.5:
            return f"Analyzing context '{context}' logically: Reason dictates valid interpretation."
        return f"Reasoning insufficient to conclude for context '{context}'."


class InterpolationAgent(Agent):
    """Agent that connects ideas or states between other agents."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, interpolation_level: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.interpolation_level = interpolation_level

    def interpolate(self, agent1: Agent, agent2: Agent) -> str:
        """Interpolate between two agents' states."""
        if self.interpolation_level > 0.5:
            return f"Interpolating between {agent1.state} and {agent2.state}: connection possible."
        return f"Unable to interpolate between {agent1.state} and {agent2.state}."


class IntercontinentalizationAgent(Agent):
    """Agent that connects agents across ontological realms."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, reach: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.reach = reach

    def connect_worlds(self, agent1: Agent, agent2: Agent) -> str:
        """Facilitate connection between two agents from different realms."""
        if self.reach > 0.5:
            return f"Connecting {agent1.state} and {agent2.state} across boundaries."
        return f"Unable to connect {agent1.state} and {agent2.state}."
