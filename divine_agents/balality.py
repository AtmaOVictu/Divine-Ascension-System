from .agent import Agent

class BalalityAgent(Agent):
    """Agent that reflects on duality while transitioning between states."""

    def reflect_on_duality(self) -> str:
        """Return a sentence describing the agent's dual nature."""
        if self.state == "Ego":
            return f"{self.name}: I am independent, but I must face the other to evolve."
        if self.state == "Jaz":
            return f"{self.name}: I relate to others, but still find myself in opposition."
        return f"{self.name}: I am unified, yet the duality within me persists."
