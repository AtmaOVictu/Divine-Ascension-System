from .agent import Agent

class OppositeSeekingAgent(Agent):
    """Agent that always seeks or generates opposition."""

    def __init__(self, name: str, symbol: str = "", state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state=state, tension=tension, emotion=emotion)
        self.symbol = symbol or name

    def find_opposition(self, statement: str) -> str:
        """Generate an opposing statement."""
        return f"Nasprotje: ne {statement}"

    def respond_to(self, other_agent: Agent, question: str) -> str:
        """Respond with opposition to another agent's answer."""
        other_reply = other_agent.respond(question)
        return self.find_opposition(other_reply)
