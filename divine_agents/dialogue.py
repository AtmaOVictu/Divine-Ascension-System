from typing import List
from .agent import Agent
from .categorizer import Categorizer


def philosophical_dialogue(agent1: Agent, agent2: Agent, categorizer: Categorizer | None = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    if categorizer:
        info = categorizer.categorize("resnica")
        if info["connotation"]:
            lines.append(
                f"Konotacija 'resnica': {info['connotation']} (kategorija: {info['category']})"
            )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Increase emotions to trigger possible transitions
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
