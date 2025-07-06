from typing import List
from datetime import datetime

from .agent import Agent
from .archive import Arhiv, Stik


def philosophical_dialogue(
    agent1: Agent, agent2: Agent, archive: Arhiv | None = None
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    if archive:
        archive.add_stik(
            Stik(agent1.name, agent2.name, "pogovor_zacetek", datetime.now())
        )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    if archive:
        archive.add_stik(
            Stik(agent1.name, agent2.name, "prehoda", datetime.now())
        )
        archive.reorganize()

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
