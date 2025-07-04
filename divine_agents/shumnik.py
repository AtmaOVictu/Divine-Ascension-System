class Shumnik:
    """Represents a symbolic trigger that influences an agent."""

    def __init__(self, symbol: str, meaning: str, effect):
        self.symbol = symbol
        self.meaning = meaning
        self.effect = effect

    def activate(self, agent) -> None:
        """Activate the shumnik's effect on the given agent."""
        self.effect(agent)


def tension_effect(agent) -> None:
    """Increase tension sufficiently to trigger a transition."""
    agent.update_tension(agent.tension + 0.8)


def reflection_effect(agent) -> None:
    """Increase emotion to encourage reflection and potential transition."""
    agent.update_emotion(agent.emotion + 0.6)


def emotional_balance_effect(agent) -> None:
    """Reduce tension and emotion to stabilize the agent."""
    agent.update_tension(max(agent.tension - 0.5, 0))
    agent.update_emotion(max(agent.emotion - 0.5, 0))
