import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parents[1]))

from divine_agents.agent import Agent


def test_cyclical_transition_sequence():
    agent = Agent("Loop", tension=0.8)
    seq = []
    for _ in range(3):
        seq.append(agent.transition())
        agent.update_emotion(0.9)
    assert seq == ["Jaz", "Enotnost", "Ego"]


def test_repeated_cycles():
    agent = Agent("Repeat", tension=0.8)
    states = []
    for _ in range(9):
        states.append(agent.transition())
        agent.update_emotion(0.9)
    expected = ["Jaz", "Enotnost", "Ego"] * 3
    assert states == expected
