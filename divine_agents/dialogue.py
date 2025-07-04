from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue influenced by emotions."""
    lines: List[str] = []

    for cycle in range(2):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        # Emotions influence tension and may trigger transitions
        agent1.feel("anger" if cycle == 0 else "joy", 0.6)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.feel("joy" if cycle == 0 else "fear", 0.7)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
