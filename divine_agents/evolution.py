from __future__ import annotations
from math import exp
from .agent import Agent


def logistic(value: float) -> float:
    """Simple logistic function used to scale tension."""
    return 1 / (1 + exp(-value))


def biological_transition(agent: Agent, stimulus: float) -> str:
    """Apply a biological stimulus to an agent and perform a state transition."""
    agent.update_emotion(stimulus)
    agent.update_tension(logistic(agent.tension))
    return agent.transition()


def social_transition(agent1: Agent, agent2: Agent) -> None:
    """Increase emotion for both agents when they are in different states."""
    if agent1.state != agent2.state:
        agent1.update_emotion(agent1.emotion + 0.6)
        agent2.update_emotion(agent2.emotion + 0.6)
