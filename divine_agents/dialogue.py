from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, max_rounds: int = 3) -> List[str]:
    """Simulate a philosophical dialogue where agents influence each other."""
    lines: List[str] = []
    rounds = 0

    while (
        rounds < max_rounds
        and agent1.state != "Enotnost"
        and agent2.state != "Enotnost"
    ):
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.feel(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.feel(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        rounds += 1

    if agent1.state == "Enotnost" or agent2.state == "Enotnost":
        lines.append("Eden od agentov je dosegel Enotnost.")
    else:
        lines.append("Dialog je končan brez dosega Enotnosti.")

    return lines
