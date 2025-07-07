from .agent import Agent
from .dialogue import philosophical_dialogue
from .special_agents import (
    RespectAgent,
    DisrespectAgent,
    FearAgent,
    OneValueAgent,
)

__all__ = [
    'Agent',
    'philosophical_dialogue',
    'RespectAgent',
    'DisrespectAgent',
    'FearAgent',
    'OneValueAgent',
]
