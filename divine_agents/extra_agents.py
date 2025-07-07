from .agent import Agent


class ReasonAgent(Agent):
    """Agent that reasons about context using a logic level."""

    def __init__(self, name: str, state: str = "Ego", logic_level: float = 0.0):
        super().__init__(name, state)
        self.logic_level = logic_level

    def update_logic(self, value: float) -> None:
        self.logic_level = min(1.0, self.logic_level + value)

    def reason(self, context: str) -> str:
        if self.logic_level > 0.5:
            return f"Analyzing '{context}' logically: valid interpretation."
        return f"Logic insufficient for '{context}'."


class InterpolationAgent(Agent):
    """Agent capable of connecting disparate states."""

    def __init__(self, name: str, state: str = "Ego", interpolation_level: float = 0.0):
        super().__init__(name, state)
        self.interpolation_level = interpolation_level

    def interpolate(self, agent1: Agent, agent2: Agent) -> str:
        if self.interpolation_level > 0.5:
            return f"Interpolating between {agent1.state} and {agent2.state}."
        return "Interpolation capacity insufficient."


class IntercontinentalizationAgent(Agent):
    """Agent that bridges ontological boundaries."""

    def __init__(self, name: str, state: str = "Ego", reach: float = 0.0):
        super().__init__(name, state)
        self.reach = reach

    def connect_worlds(self, agent1: Agent, agent2: Agent) -> str:
        if self.reach > 0.5:
            return f"Connecting {agent1.state} and {agent2.state} across realms."
        return "Reach insufficient to connect worlds."

