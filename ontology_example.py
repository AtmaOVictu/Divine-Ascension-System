"""Example simulation using ontological agents.

Agents transition between states (Ego, Jaz, Enotnost) when their tension or emotion exceeds
predefined thresholds. Each state reflects a different view on truth:
- Ego: truth is absolute.
- Jaz: truth is relative.
- Enotnost: all truths are unified.
"""

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def main():
    """Run a simple ontological simulation between two agents."""
    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2", state="Jaz")

    dialogue_lines = philosophical_dialogue(agent1, agent2)
    for line in dialogue_lines:
        print(line)


if __name__ == "__main__":
    main()
