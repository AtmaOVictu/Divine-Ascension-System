from .agent import Agent

class ReasonAgent(Agent):
    """Agent that uses reason to interpret context and make logical conclusions."""

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0, logic_level: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.logic_level = logic_level

    def update_logic(self, value: float) -> None:
        """Increase logic level up to a maximum of 1.0."""
        self.logic_level += value
        if self.logic_level > 1.0:
            self.logic_level = 1.0

    def reason(self, context: str) -> str:
        """Return a reasoning statement depending on logic level."""
        if self.logic_level > 0.5:
            return f"Analiziram '{context}': razumski sklep je veljaven."
        return f"Logična raven prenizka za sklep o '{context}'."
