import argparse
from .agent import Agent
from .dialogue import philosophical_dialogue


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Run a philosophical dialogue between two agents.")

    parser.add_argument("--name1", default="Agent1", help="Name of first agent")
    parser.add_argument("--state1", default="Ego",
                        choices=Agent.STATES, help="Initial state of first agent")
    parser.add_argument("--tension1", type=float, default=0.0,
                        help="Initial tension of first agent")
    parser.add_argument("--emotion1", type=float, default=0.0,
                        help="Initial emotion of first agent")

    parser.add_argument("--name2", default="Agent2", help="Name of second agent")
    parser.add_argument("--state2", default="Ego",
                        choices=Agent.STATES, help="Initial state of second agent")
    parser.add_argument("--tension2", type=float, default=0.0,
                        help="Initial tension of second agent")
    parser.add_argument("--emotion2", type=float, default=0.0,
                        help="Initial emotion of second agent")

    args = parser.parse_args()

    agent1 = Agent(args.name1, state=args.state1,
                   tension=args.tension1, emotion=args.emotion1)
    agent2 = Agent(args.name2, state=args.state2,
                   tension=args.tension2, emotion=args.emotion2)

    for line in philosophical_dialogue(agent1, agent2):
        print(line)


if __name__ == "__main__":
    main()
