import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from divine_agents.agent import Agent


def test_agent_state_transition():
    agent = Agent("Luka", state="Ego", tension=0.8)
    agent.update_emotion("anger", 0.8) if False else None  # placeholder for mocking example, but we call transition after update
    agent.update_emotion(0.8)
    state_after_transition = agent.transition()
    assert state_after_transition == "Jaz"


def test_agent_emotion_response():
    agent = Agent("Ana", state="Jaz", tension=0.9)
    agent.update_emotion(0.9)
    state_after_transition = agent.transition()
    assert state_after_transition == "Enotnost"


def test_agent_loop():
    agent = Agent("Luka", state="Ego", tension=0.9)
    agent.update_emotion(0.9)
    assert agent.transition() == "Jaz"

    agent.update_emotion(0.9)
    assert agent.transition() == "Enotnost"

    agent.update_emotion(0.8)
    assert agent.transition() == "Enotnost"


def test_infinite_cycles(monkeypatch):
    agent = Agent("Luka", state="Ego", tension=0.5)
    transitions = []

    original_transition = agent.transition

    def wrapped_transition():
        result = original_transition()
        transitions.append(result)
        return result

    monkeypatch.setattr(agent, "transition", wrapped_transition)

    for _ in range(10):
        agent.update_emotion(0.8)
        agent.transition()

    expected = ["Jaz"] + ["Enotnost"] * 9
    assert transitions == expected
