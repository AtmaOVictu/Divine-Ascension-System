from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def main() -> None:
    """Execute a sample dialogue between two agents."""
    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2", state="Jaz")

    for line in philosophical_dialogue(agent1, agent2):
        print(line)


if __name__ == "__main__":
    main()
