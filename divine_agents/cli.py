"""Command line interface for running a philosophical debate between agents."""

from argparse import ArgumentParser
from typing import List

from .agent import Agent
from .dialogue import philosophical_dialogue


def run_dialogue(
    name1: str = "A1",
    state1: str = "Ego",
    name2: str = "A2",
    state2: str = "Jaz",
) -> List[str]:
    """Create agents and run a philosophical dialogue.

    Parameters
    ----------
    name1, state1 : str
        Initial name and ontological state for the first agent.
    name2, state2 : str
        Initial name and ontological state for the second agent.

    Returns
    -------
    List[str]
        Dialogue lines produced during the interaction.
    """

    agent1 = Agent(name1, state=state1)
    agent2 = Agent(name2, state=state2)
    return philosophical_dialogue(agent1, agent2)


def main(argv: list | None = None) -> None:
    """Entry point for the CLI."""

    parser = ArgumentParser(description="Run a philosophical debate between two agents.")
    parser.add_argument("--name1", default="A1", help="Name of the first agent")
    parser.add_argument(
        "--state1",
        default="Ego",
        choices=Agent.STATES,
        help="Ontological state of the first agent",
    )
    parser.add_argument("--name2", default="A2", help="Name of the second agent")
    parser.add_argument(
        "--state2",
        default="Jaz",
        choices=Agent.STATES,
        help="Ontological state of the second agent",
    )

    args = parser.parse_args(argv)

    lines = run_dialogue(args.name1, args.state1, args.name2, args.state2)
    for line in lines:
        print(line)


if __name__ == "__main__":  # pragma: no cover - manual invocation
    main()

