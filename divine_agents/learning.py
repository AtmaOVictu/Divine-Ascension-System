class ExperienceBasedLearning:
    """Simple learner that adjusts decisions based on past experiences."""

    def __init__(self, agent):
        self.agent = agent

    def learn_from_past_decisions(self, situation: str) -> str:
        """Return a decision suggestion based on agent's history."""
        if situation == "danger":
            if "helped" in self.agent.experiences:
                return "Act selflessly"
            return "Self-preservation"
        return "Neutral decision"
