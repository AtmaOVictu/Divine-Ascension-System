from typing import Callable

from .agent import Agent


class Shumnik:
    """Symbolic tool influencing agent states."""

    def __init__(self, symbol: str, meaning: str, effect: Callable[[Agent], None]):
        self.symbol = symbol
        self.meaning = meaning
        self.effect = effect

    def activate(self, agent: Agent) -> None:
        """Trigger the shumnik's effect on the given agent."""
        self.effect(agent)


# Example effects for default shumniki

def tension_effect(agent: Agent) -> None:
    """Increase agent tension."""
    agent.update_tension(agent.tension + 0.3)


def reflection_effect(agent: Agent) -> None:
    """Encourage reflection by slightly increasing emotion."""
    agent.update_emotion(agent.emotion + 0.2)


def emotional_balance_effect(agent: Agent) -> None:
    """Bring the agent to emotional balance by lowering tension."""
    agent.update_tension(max(agent.tension - 0.3, 0.0))
