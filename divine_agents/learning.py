class ExperienceBasedLearning:
    """Simple reinforcement learning using past experiences."""

    def __init__(self, agent):
        self.agent = agent
        self.q_table = {}

    def update_experience(self, situation, reward):
        key = (self.agent.state, situation)
        self.q_table[key] = self.q_table.get(key, 0) + reward

    def decide(self, situation):
        key = (self.agent.state, situation)
        return "Act selflessly" if self.q_table.get(key, 0) > 0 else "Self-preservation"

