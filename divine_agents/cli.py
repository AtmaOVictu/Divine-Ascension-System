import argparse
from .agent import Agent
from .dialogue import philosophical_dialogue


def main() -> None:
    """Command-line interface to run a philosophical dialogue."""
    parser = argparse.ArgumentParser(description="Simulate a philosophical dialogue between two agents.")
    parser.add_argument("--agent1", default="Agent1", help="Name of the first agent (starts in Ego state)")
    parser.add_argument("--agent2", default="Agent2", help="Name of the second agent (starts in Jaz state)")
    args = parser.parse_args()

    a1 = Agent(args.agent1, state="Ego")
    a2 = Agent(args.agent2, state="Jaz")

    for line in philosophical_dialogue(a1, a2):
        print(line)


if __name__ == "__main__":
    main()
