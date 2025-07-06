"""Agent generation utilities following OS GENESSZTA concept."""
import random
from .agent import Agent

class AgentGenerator:
    """Generate new agents with randomised attributes."""

    def __init__(self, agent_type: str = "default") -> None:
        self.agent_type = agent_type

    def generate_agent(self) -> Agent:
        """Create a new agent and assign customised properties."""
        name = f"Agent_{random.randint(1, 100)}"
        emotional_state = random.choice(["happy", "fearful", "neutral"])
        loyalty = random.uniform(0, 1)

        agent = Agent(name)
        agent.emotional_state = emotional_state
        agent.loyalty = loyalty
        return agent
