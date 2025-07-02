from .agents import Agent


def simulate_philosophical_dialogue():
    """Run a simple multi-agent discussion about truth."""
    agent1 = Agent(name="Agent 1", state="Ego")
    agent2 = Agent(name="Agent 2", state="Jaz")
    agent3 = Agent(name="Agent 3", state="Enotnost")

    agents = [agent1, agent2, agent3]
    print("Philosophical Debate on Absolute Truths:\n")
    for agent in agents:
        response = agent.interact(agents, "philosophy")
        print(response)


if __name__ == "__main__":
    simulate_philosophical_dialogue()
