"""Module providing a simple philosophical dialogue between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotion."""

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent1 reacts with anger to Agent2's statement
    agent1.set_emotion("jezo", 0.6)
    lines.append(f"{agent1.name}: {agent1.respond('Ne strinjam se!')}")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 responds with joy which elevates its tension
    agent2.set_emotion("veselje", 0.8)
    lines.append(f"{agent2.name}: {agent2.respond('Zanimivo razmisljanje.')}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
