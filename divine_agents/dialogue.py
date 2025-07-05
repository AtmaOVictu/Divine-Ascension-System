from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, cycles: int = 1) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Agents respond according to their current ontological state. After each round
    of responses, they simultaneously perform ``ora_et_labora`` which may cause
    state transitions based on their updated emotions and tension.
    """
    lines: List[str] = []
    for _ in range(cycles):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        lines.append(agent1.ora_et_labora(0.8, 0.8))
        lines.append(agent2.ora_et_labora(0.6, 0.6))
    return lines
