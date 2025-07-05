from typing import List

from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    lang1: str | None = None,
    lang2: str | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Optionally change their languages before the conversation."""

    if lang1:
        agent1.change_language(lang1)
    if lang2:
        agent2.change_language(lang2)

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
