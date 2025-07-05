from typing import List
from .agent import Agent


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


def regenerative_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Dialogue that utilizes the Regeneration process."""
    from .regeneration import Regeneration

    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    regen1 = Regeneration(agent1)
    lines.append(f"{agent1.name} prehaja v stanje: {regen1.progress()}")

    agent2.update_emotion(0.4)
    regen2 = Regeneration(agent2)
    lines.append(f"{agent2.name} ostaja v stanju: {regen2.progress()}")

    agent2.update_emotion(0.4)
    lines.append(f"{agent2.name} prehaja v stanje: {regen2.progress()}")
    lines.append(f"{agent2.name} prehaja v stanje: {regen2.progress()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
