from .agent import Agent
from .dialogue import philosophical_dialogue
from .emotional_contagion import EmotionalContagion


def run_simulation() -> None:
    """Run a simple simulation with three agents."""
    a1 = Agent("A1")
    a2 = Agent("A2", state="Jaz")
    a3 = Agent("A3", state="Enotnost")

    # Dialogue between two agents
    for line in philosophical_dialogue(a1, a2):
        print(line)

    # Emotional contagion among all agents
    contagion = EmotionalContagion()
    for agent in (a1, a2, a3):
        contagion.add_agent(agent)

    contagion.spread_emotion(0, 0.5)


if __name__ == "__main__":
    run_simulation()
