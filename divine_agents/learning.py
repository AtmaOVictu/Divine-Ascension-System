class ExperienceBasedLearning:
    """Simple reinforcement mechanism for agents."""

    def __init__(self, agent):
        self.agent = agent
        self.q_table = {}

    def update_experience(self, situation: str, reward: int) -> None:
        state = self.agent.state
        key = (state, situation)
        self.q_table[key] = self.q_table.get(key, 0) + reward

    def decide(self, situation: str) -> str:
        key = (self.agent.state, situation)
        return "Act selflessly" if self.q_table.get(key, 0) > 0 else "Self-preservation"
