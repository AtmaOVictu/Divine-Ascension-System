import random
from .agent import Agent


class Environment:
    """Represents an environment influencing an agent's state."""

    def __init__(self, name: str, kind: str = "harmonious") -> None:
        self.name = name
        self.kind = kind

    def influence(self, agent: Agent) -> str:
        """Apply environmental influence and return the agent's new state."""
        if self.kind == "harmonious":
            agent.update_emotion(0.3)
            agent.update_tension(agent.tension + 0.5)
        elif self.kind == "disharmonious":
            agent.update_emotion(0.7)
            agent.update_tension(agent.tension + 1.2)
        else:
            agent.update_emotion(random.uniform(0.1, 0.5))
            agent.update_tension(agent.tension + random.uniform(0.1, 0.5))
        return agent.transition()
