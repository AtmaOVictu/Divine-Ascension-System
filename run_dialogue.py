from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def main() -> None:
    """Run a sample philosophical dialogue between two agents."""
    agent1 = Agent("A1")
    agent2 = Agent("A2", state="Jaz")
    for line in philosophical_dialogue(agent1, agent2):
        print(line)


if __name__ == "__main__":
    main()
