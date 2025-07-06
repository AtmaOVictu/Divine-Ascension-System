from typing import List
from .agent import Agent
from .emotional_contagion import EmotionalContagion


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def run_simulation() -> List[str]:
    """Run a small example simulation with three agents."""
    a1 = Agent("A1")
    a2 = Agent("A2", state="Jaz")
    a3 = Agent("A3", state="Enotnost")

    lines = philosophical_dialogue(a1, a2)

    ec = EmotionalContagion()
    ec.add_agent(a1)
    ec.add_agent(a2)
    ec.add_agent(a3)
    ec.spread_emotion(0, 0.5)

    return lines

