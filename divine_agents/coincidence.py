"""Happy coincidence utilities for agents.

This module implements the concept that "There are no accidents, only happy coincidences".
It provides functionality to randomly generate events between agents that may
influence their emotions and tensions, potentially triggering state transitions.
"""

from __future__ import annotations

import random
from typing import Tuple

from .agent import Agent

COINCIDENCE_EVENTS = ["positive", "neutral", "conflict", "surprise", "happy"]


def happy_coincidence(agent1: Agent, agent2: Agent) -> Tuple[str, str, str]:
    """Generate a happy coincidence between two agents.

    Parameters
    ----------
    agent1 : Agent
        First agent participating in the event.
    agent2 : Agent
        Second agent participating in the event.

    Returns
    -------
    Tuple[str, str, str]
        The event description and the resulting states of both agents.
    """
    event = random.choice(COINCIDENCE_EVENTS)

    if event == "positive":
        # a positive coincidence uplifts both agents
        agent1.update_emotion(0.6)
        agent2.update_emotion(0.6)
    elif event == "conflict":
        # a conflict increases tension without exceeding emotion threshold
        agent1.update_emotion(0.4)
        agent2.update_emotion(0.4)
    else:
        # neutral or surprising events have moderate effect
        agent1.update_emotion(0.3)
        agent2.update_emotion(0.3)

    state1 = agent1.transition()
    state2 = agent2.transition()
    return event, state1, state2
