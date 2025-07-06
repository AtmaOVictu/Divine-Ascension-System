from divine_agents.agent import Agent
from divine_agents.dialogue import philosophical_dialogue


def main() -> None:
    """Demonstrate agent interactions and state transitions."""
    agent1 = Agent("A1")  # Starts in Ego
    agent2 = Agent("A2", state="Jaz")

    print(f"Initial states: {agent1.name}={agent1.state}, {agent2.name}={agent2.state}")

    # First interaction
    lines = philosophical_dialogue(agent1, agent2)
    for line in lines:
        print(line)
    print(f"After first interaction: {agent1.name}={agent1.state}, {agent2.name}={agent2.state}")

    # Second interaction
    lines = philosophical_dialogue(agent1, agent2)
    for line in lines:
        print(line)
    print(f"After second interaction: {agent1.name}={agent1.state}, {agent2.name}={agent2.state}")


if __name__ == "__main__":
    main()
