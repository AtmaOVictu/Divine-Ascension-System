from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def main() -> None:
    """Create two agents and run a short philosophical dialogue."""
    agent1 = Agent("Ada")
    agent2 = Agent("Blaise", state="Jaz")

    for line in philosophical_dialogue(agent1, agent2):
        print(line)


if __name__ == "__main__":
    main()
