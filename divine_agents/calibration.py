from typing import Iterable
from .agent import Agent


def calibrate_tensions(agents: Iterable[Agent], factor: float) -> None:
    """Scale tension of each agent by a given factor."""
    for agent in agents:
        agent.tension *= factor

