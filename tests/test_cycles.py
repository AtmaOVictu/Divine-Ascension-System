import pytest
from divine_agents.agent import Agent


def test_agent_state_transition():
    agent = Agent("Luka", state="Ego", tension=0.8)
    agent.update_emotion("anger", 0.8)
    assert agent.transition() == "Jaz"


def test_agent_emotion_response():
    agent = Agent("Ana", state="Jaz", tension=0.9)
    agent.update_emotion("joy", 0.9)
    assert agent.transition() == "Enotnost"


def test_agent_loop():
    agent = Agent("Luka", state="Ego", tension=0.9)
    agent.update_emotion("anger", 0.9)
    assert agent.transition() == "Jaz"

    agent.update_emotion("joy", 0.9)
    assert agent.transition() == "Enotnost"

    agent.update_emotion("calm", 0.8)
    assert agent.transition() == "Ego"


def test_infinite_cycles():
    agent = Agent("Luka", state="Ego", tension=0.5)
    states = []
    for _ in range(10):
        agent.update_emotion("anger", 0.8)
        states.append(agent.transition())

    pattern = ["Jaz", "Enotnost", "Ego"]
    expected = [pattern[i % 3] for i in range(10)]
    assert states == expected

