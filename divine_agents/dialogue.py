from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise as discussion continues
    agent1.update_emotion(0.4, "anger")
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Zakaj verjames v svojo resnico?')}"
    )

    agent2.update_emotion(0.3, "joy")
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Resnica je lahko drugacna za vsakega.')}"
    )

    # Tension escalates leading to transitions
    agent1.update_emotion(0.8, "fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.7, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa zdaj mislis o resnici?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Ali obstaja ena resnica?')}"
    )

    return lines
