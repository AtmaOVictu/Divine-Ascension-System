"""Divine Agents package."""

from .agent import Agent
from .dialogue import philosophical_dialogue
from .res_states import RES_STATES, RES_SEQUENCE, ResState
from .process_e import simulate_process_e

__all__ = [
    "Agent",
    "philosophical_dialogue",
    "RES_STATES",
    "RES_SEQUENCE",
    "ResState",
    "simulate_process_e",
]
