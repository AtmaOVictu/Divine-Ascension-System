import pytest
from divine_agents.agent import AgentWithShadow


def test_tension_increase_with_shadow():
    agent = AgentWithShadow("S")
    assert agent.get_tension() == 0
    agent.update_emotion(5, -2)
    assert agent.get_tension() == 3
    agent.update_emotion(10, -3)
    assert agent.get_tension() == 10
