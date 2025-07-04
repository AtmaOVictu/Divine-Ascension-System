import random
from .agent import Agent


class Simulation:
    """Simulate future state transitions based on slight changes in tension and emotion."""

    def simulate_future_state(self, agent: Agent) -> str:
        """Return the predicted next state for an agent."""
        temp = Agent(agent.name, state=agent.state, tension=agent.tension, emotion=agent.emotion)
        temp.update_tension(min(1.0, agent.tension + random.uniform(0.1, 0.3)))
        temp.update_emotion(min(1.0, agent.emotion + random.uniform(0.0, 0.2)))
        return temp.transition()


class SpeculativeAgent(Agent):
    """Agent that speculates about truth based on its current ontological state."""

    def speculate(self, statement: str) -> str:
        base = self.respond(statement)
        if self.state == "Ego":
            return f"Morda {statement}, toda verjamem, da {base}"
        if self.state == "Jaz":
            return f"Morda {statement}, a za nas je resnica, da {base}"
        return f"Morda {statement}, vendar v resnici {base}"
