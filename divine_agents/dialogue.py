from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.zaznaj_problem("Iskanje globljega razumevanja")
    agent2.zaznaj_problem("Povezovanje z drugimi agenti")

    agent1.resi_problem()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    agent2.resi_problem()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    agent1.dialog(agent2)

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
