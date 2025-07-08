from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with optional monologues.

    Agents may express a self-reflective monologue before and after the main
    exchange if their emotional state or tension crosses the defined
    thresholds.
    """
    lines: List[str] = []

    for agent in (agent1, agent2):
        monologue = agent.start_monologue()
        if monologue:
            lines.append(monologue)

    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    monologue = agent1.start_monologue()
    if monologue:
        lines.append(monologue)

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    monologue = agent2.start_monologue()
    if monologue:
        lines.append(monologue)

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
