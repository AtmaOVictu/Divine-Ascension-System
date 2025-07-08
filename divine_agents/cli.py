"""Command-line interface for philosophical dialogue."""

import argparse
from .agent import Agent
from .dialogue import philosophical_dialogue


def main() -> None:
    """Run a sample dialogue between two agents."""
    parser = argparse.ArgumentParser(description="Run a philosophical dialogue between two agents.")
    parser.add_argument("--state1", default="Ego", choices=Agent.STATES, help="Initial state of Agent1")
    parser.add_argument("--state2", default="Ego", choices=Agent.STATES, help="Initial state of Agent2")
    parser.add_argument("--tension1", type=float, default=0.0, help="Initial tension of Agent1")
    parser.add_argument("--tension2", type=float, default=0.0, help="Initial tension of Agent2")
    parser.add_argument("--emotion1", type=float, default=0.0, help="Initial emotion of Agent1")
    parser.add_argument("--emotion2", type=float, default=0.0, help="Initial emotion of Agent2")
    args = parser.parse_args()

    agent1 = Agent("Agent1", state=args.state1, tension=args.tension1, emotion=args.emotion1)
    agent2 = Agent("Agent2", state=args.state2, tension=args.tension2, emotion=args.emotion2)

    lines = philosophical_dialogue(agent1, agent2)
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
