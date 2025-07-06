"""Learning and adjustment utilities for agents."""


class ExperienceBasedLearning:
    """Simple Q-learning like helper for agents."""

    def __init__(self, agent):
        self.agent = agent
        self.q_table = {}

    def update_experience(self, situation: str, reward: int) -> None:
        key = (self.agent.state, situation)
        self.q_table[key] = self.q_table.get(key, 0) + reward

    def decide(self, situation: str) -> str:
        key = (self.agent.state, situation)
        return "Act selflessly" if self.q_table.get(key, 0) > 0 else "Self-preservation"


class HistoricalRefactor:
    """Analyze agent history to give simple feedback."""

    def __init__(self, agent):
        self.agent = agent

    def auto_refactor(self) -> str:
        history = self.agent.history[-3:]
        if "hesitation" in history:
            return "Prehod v Jaz zaradi negotovosti."
        if "self-preservation" in self.agent.experiences:
            return "Agent ostaja v Egu zaradi sebičnosti."
        return "Stanje je stabilno, prehod ni potreben."


class EmotionalTensionDynamics:
    """Adjust agent tension based on named emotional state."""

    def __init__(self, agent):
        self.agent = agent

    def adjust_tension(self) -> None:
        state = self.agent.emotional_state
        if state == "angry":
            self.agent.tension += 0.3
        elif state == "happy":
            self.agent.tension -= 0.2
        else:
            self.agent.tension += 0.1
