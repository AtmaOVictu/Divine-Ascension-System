from typing import List, Tuple
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion_mods: tuple[float, float] = (0.0, 0.0),
    tension_mods: tuple[float, float] = (0.0, 0.0),
) -> List[Tuple[str, str]]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[Tuple[str, str]] = []
    lines.append((agent1.name, agent1.respond("Kaj je resnica?")))
    lines.append((agent2.name, agent2.respond("Kaj je resnica?")))

    agent1.update_emotion(emotion_mods[0])
    if tension_mods[0]:
        agent1.update_tension(agent1.tension + tension_mods[0])
    lines.append((agent1.name, f"prehaja v stanje: {agent1.transition()}"))

    agent2.update_emotion(emotion_mods[1])
    if tension_mods[1]:
        agent2.update_tension(agent2.tension + tension_mods[1])
    lines.append((agent2.name, f"prehaja v stanje: {agent2.transition()}"))

    lines.append((agent1.name, agent1.respond("Kaj je resnica?")))
    lines.append((agent2.name, agent2.respond("Kaj je resnica?")))
    return lines
