class ExperienceBasedLearning:
    """Simple reinforcement learning placeholder."""

    def __init__(self, agent):
        self.agent = agent
        self.q_table = {}

    def update_experience(self, situation: str, reward: int) -> None:
        state = self.agent.state
        key = (state, situation)
        self.q_table[key] = self.q_table.get(key, 0) + reward

    def decide(self, situation: str) -> str:
        key = (self.agent.state, situation)
        return "altruistic" if self.q_table.get(key, 0) > 0 else "self-preservation"


class HistoricalRefactor:
    """Analyse history and provide textual feedback."""

    def __init__(self, agent):
        self.agent = agent

    def auto_refactor(self) -> str:
        if "hesitation" in self.agent.history[-3:]:
            return "Prehod v Jaz zaradi negotovosti."
        elif "self-preservation" in self.agent.experiences:
            return "Agent ostaja v Egu zaradi sebičnosti."
        else:
            return "Stanje je stabilno, prehod ni potreben."


class EmotionalTensionDynamics:
    """Adjust tension depending on labelled emotional state."""

    def __init__(self, agent):
        self.agent = agent

    def adjust_tension(self) -> None:
        label = getattr(self.agent, "emotional_state", "neutral")
        if label == "angry":
            self.agent.tension += 0.3
        elif label == "happy":
            self.agent.tension -= 0.2
        else:
            self.agent.tension += 0.1
