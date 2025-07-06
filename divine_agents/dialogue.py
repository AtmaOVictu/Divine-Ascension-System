from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, max_rounds: int = 10) -> List[str]:
    """Simulate a philosophical dialogue with evolving emotions."""
    lines: List[str] = []

    round_no = 0
    while round_no < max_rounds and "Enotnost" not in (agent1.state, agent2.state):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.feel(0.1)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.feel(0.1)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        round_no += 1

    if "Enotnost" in (agent1.state, agent2.state):
        lines.append("Eden od agentov je dosegel Enotnost.")
    else:
        lines.append("Dialog je končan brez dosega Enotnosti.")

    return lines
