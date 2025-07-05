from typing import List, Set, Tuple
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, max_turns: int = 5) -> List[str]:
    """Simulate a philosophical dialogue ensuring no infinite loops."""
    lines: List[str] = []
    visited: Set[Tuple[str, str]] = set()

    for _ in range(max_turns):
        pair = (agent1.state, agent2.state)
        if pair in visited:
            lines.append("Zanka ustavljena.")
            break
        visited.add(pair)

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
