from typing import List

from .agent import Agent
from .metaparadox import MetaparadoxicalModule
from .absolutes import RelativeAbsoluteLibrary


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    library = RelativeAbsoluteLibrary()
    meta1 = MetaparadoxicalModule(agent1)
    meta2 = MetaparadoxicalModule(agent2)
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Introduce a relative absolute for flavor
    lines.append(f"Sistem: relativna resnica = {library.get_absolute('truth'):.2f}")

    # Update emotions and perform paradoxical transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {meta1.paradoxical_transition()}")

    # Agent 2 experiences stronger emotions leading to higher tension
    agent2.update_emotion(0.9)
    lines.append(f"{agent2.name} prehaja v stanje: {meta2.paradoxical_transition()}")

    # Agents respond again from new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
