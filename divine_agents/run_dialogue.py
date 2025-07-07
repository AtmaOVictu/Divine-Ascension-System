"""Command line interface for running philosophical dialogues between agents."""

import argparse
from .agent import Agent
from .dialogue import philosophical_dialogue


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Run a philosophical dialogue between agents")
    parser.add_argument("--name1", required=True, help="Name of the first agent")
    parser.add_argument("--name2", required=True, help="Name of the second agent")
    parser.add_argument("--state1", default="Ego", help="Initial state of the first agent")
    parser.add_argument("--state2", default="Jaz", help="Initial state of the second agent")
    return parser.parse_args(args)


def main(args=None):
    """Entry point for the CLI."""
    options = parse_args(args)
    agent1 = Agent(options.name1, state=options.state1)
    agent2 = Agent(options.name2, state=options.state2)

    lines = philosophical_dialogue(agent1, agent2)
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
