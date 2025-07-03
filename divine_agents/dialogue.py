from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional updates triggering potential transitions
    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} čuti intenzivna čustva ({agent1.emotion}) in prehaja v: {agent1.transition()}"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} čuti intenzivna čustva ({agent2.emotion}) in prehaja v: {agent2.transition()}"
    )

    # Final statements after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Include ontological values for reference
    lines.append(f"{agent1.name} nomen: {agent1.nomen}")
    lines.append(f"{agent2.name} nomen: {agent2.nomen}")

    return lines
