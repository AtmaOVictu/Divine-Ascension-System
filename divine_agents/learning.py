"""Experience-based learning helpers."""

from .agent import Agent

class ExperienceBasedLearning:
    """Simple experience-driven decision helper."""

    def __init__(self, agent: Agent) -> None:
        self.agent = agent

    def learn_from_experience(self, situation: str) -> str:
        """Return advice based on agent history and situation."""
        history = self.agent.history
        if situation == "danger":
            if "helped" in history:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"
