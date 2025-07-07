from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def main() -> None:
    """Run a simple philosophical debate between two agents."""
    agent1 = Agent("Agent 1")
    agent2 = Agent("Agent 2", state="Jaz")

    lines = philosophical_dialogue(agent1, agent2)
    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
