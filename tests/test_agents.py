import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.agents import Agent


def test_philosophical_dialogue_multi_agent():
    agent1 = Agent(name="Agent 1", state="Ego")
    agent2 = Agent(name="Agent 2", state="Jaz")
    agent3 = Agent(name="Agent 3", state="Enotnost")

    dialogue = agent1.interact([agent2, agent3], "philosophy")

    assert "absolute" in dialogue
    assert "relative" in dialogue
    assert "one" in dialogue
