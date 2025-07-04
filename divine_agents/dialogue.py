from typing import List, Sequence, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions1: Sequence[Tuple[str, float]],
    emotions2: Sequence[Tuple[str, float]],
) -> List[str]:
    """Simulate a philosophical dialogue where emotions drive transitions."""

    lines: List[str] = []
    cycles = min(len(emotions1), len(emotions2))

    for i in range(cycles):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        e1, v1 = emotions1[i]
        e2, v2 = emotions2[i]
        agent1.update_emotion(v1, e1)
        agent2.update_emotion(v2, e2)

        new_state1 = agent1.transition()
        new_state2 = agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Final reflection after transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
