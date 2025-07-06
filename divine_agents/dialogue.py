from typing import List
from .agent import Agent
from .phonetics import process_sound


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def phonetic_dialogue(agent1: Agent, agent2: Agent, sounds: List[str]) -> List[str]:
    """Simulate dialogue driven by phonetic sounds."""
    lines: List[str] = []
    agents = [agent1, agent2]
    for i, sound in enumerate(sounds):
        speaker = agents[i % 2]
        lines.append(f"{speaker.name} izgovori '{sound}'")
        new_state = process_sound(speaker, sound)
        lines.append(f"{speaker.name} prehaja v stanje: {new_state}")
        lines.append(f"{speaker.name} ({speaker.state}): {speaker.respond('Kaj je resnica?')}")
    return lines
