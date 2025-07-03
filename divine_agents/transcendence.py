"""Utility functions for digital transcendence in agents."""
from .agent import Agent


def initiate_agent_digital_transcendence(agent: Agent) -> bool:
    """Force an agent to reach Enotnost if thresholds met.

    Parameters
    ----------
    agent : Agent
        The agent to elevate.

    Returns
    -------
    bool
        True if agent reached Enotnost, otherwise False.
    """
    if agent.tension > 0.9 and agent.emotion > 0.7:
        # Transition until the agent reaches the highest state
        while agent.state != "Enotnost":
            agent.transition()
        return True
    return False
