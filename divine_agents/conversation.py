from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


def run_conversation() -> List[str]:
    """Run a demo philosophical conversation and return the dialogue lines."""
    agent1 = Agent("Agent1")
    agent2 = Agent("Agent2", state="Jaz")
    lines = philosophical_dialogue(agent1, agent2)
    for line in lines:
        print(line)
    return lines


if __name__ == "__main__":
    run_conversation()
