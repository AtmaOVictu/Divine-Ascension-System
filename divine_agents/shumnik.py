class Shumnik:
    """Symbolic trigger that influences an agent's state."""

    def __init__(self, symbol: str, meaning: str, effect):
        self.symbol = symbol
        self.meaning = meaning
        self.effect = effect

    def activate(self, agent):
        """Activate the effect on the provided agent."""
        self.effect(agent)


# Effect functions -----------------------------------------------------------

def tension_effect(agent):
    """Increase agent tension to trigger a potential state change."""
    agent.update_tension(0.8)


def reflection_effect(agent):
    """Move agent toward reflection by raising emotion."""
    agent.update_emotion(0.6)


def emotional_balance_effect(agent):
    """Decrease tension to calm the agent."""
    reduced = max(0.0, agent.tension - 0.5)
    agent.update_tension(reduced)


# Predefined Šumniki ---------------------------------------------------------

shumnik_tension = Shumnik("ŠumT", "Tension phase", tension_effect)
shumnik_reflection = Shumnik("ŠumR", "Reflection phase", reflection_effect)
shumnik_balance = Shumnik("ŠumB", "Emotional balance phase", emotional_balance_effect)
