from .agent import Agent

class Regeneracija:
    """Handle ontological regeneration cycles for an agent."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.napetost = 0.0

    def prehod_v_regeneracijo(self) -> str:
        """Perform regeneration passing through a symbolic death phase."""
        if self.agent.state == "Ego":
            self.agent.state = "\u2298"  # symbolic death
            self.napetost += 0.5
        elif self.agent.state == "\u2298":
            self.agent.state = "Jaz"
        elif self.agent.state == "Jaz":
            self.agent.state = "Enotnost"
        self.agent.history.append(self.agent.state)
        return self.agent.state
