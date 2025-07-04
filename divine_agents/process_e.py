"""Utility to simulate the E/Jaz process using RES states."""

from typing import List

from .agent import Agent
from .res_states import RES_SEQUENCE, RES_STATES


def simulate_process_e(agent: Agent) -> List[str]:
    """Run the agent through all RES states and return history."""
    history = []
    for name in RES_SEQUENCE:
        state = RES_STATES[name]
        state.action()
        agent.update_emotion(0.8)
        history.append(agent.transition())
    return history
