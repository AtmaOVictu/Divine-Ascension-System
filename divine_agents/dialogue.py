from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical debate influenced by emotion."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.dialogue_line('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.dialogue_line('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.dialogue_line('Kaj je resnica?')}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.dialogue_line('Kaj je resnica?')}")

    return lines
