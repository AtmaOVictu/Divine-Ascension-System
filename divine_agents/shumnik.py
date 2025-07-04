class Shumnik:
    """Symbolic tool influencing agent states."""

    def __init__(self, symbol: str, meaning: str, effect):
        self.symbol = symbol
        self.meaning = meaning
        self.effect = effect

    def activate(self, agent):
        """Apply the effect to the given agent."""
        self.effect(agent)


def tension_effect(agent):
    """Increase agent tension."""
    agent.update_tension(agent.tension + 0.8)


def reflection_effect(agent):
    """Increase emotion leading to reflection."""
    agent.update_emotion(min(1.0, agent.emotion + 0.6))


def emotional_balance_effect(agent):
    """Reduce tension and emotion to balance the agent."""
    agent.update_tension(max(0.0, agent.tension - 0.5))
    agent.emotion = max(0.0, agent.emotion - 0.3)
