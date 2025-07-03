"""Codex Agent Framework

This package implements the dynamic agent-based ontological system.
Agents transition between Ego, Jaz, and Enotnost states according
to their emotional intensity and tension. The framework exposes
three main modules:

- :mod:`divine_agents.agent` provides the :class:`~divine_agents.agent.Agent`
  class implementing state transitions and responses.
- :mod:`divine_agents.dialogue` supplies :func:`~divine_agents.dialogue.philosophical_dialogue`
  for running a sample conversation between agents.

Utility helpers such as :func:`initialize_agents` make it easy to
create agents for simulation or tests.
"""

from .agent import Agent
from .dialogue import philosophical_dialogue


def initialize_agents():
    """Return a pair of default agents for quick experimentation."""
    agent1 = Agent("Agent1")
    agent2 = Agent("Agent2", state="Jaz")
    return agent1, agent2
