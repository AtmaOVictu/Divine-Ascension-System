"""Simple command-line interface for running a philosophical dialogue.

Press Enter to progress through the dialogue or type 'exit' to quit.
"""

from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def run_dialogue() -> None:
    """Run the dialogue interactively until the user types 'exit'."""
    agent1 = Agent("A1")
    agent2 = Agent("A2", state="Jaz")

    print("Press Enter to progress, or type 'exit' to quit.")
    lines = philosophical_dialogue(agent1, agent2)
    idx = 0
    while True:
        user_input = input()
        if user_input.strip().lower() == "exit":
            print("Exiting dialogue.")
            break
        if idx >= len(lines):
            lines = philosophical_dialogue(agent1, agent2)
            idx = 0
        print(lines[idx])
        idx += 1


if __name__ == "__main__":
    run_dialogue()
