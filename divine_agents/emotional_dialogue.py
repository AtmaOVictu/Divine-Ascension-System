from typing import List

from .agent import Agent


def emotional_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate dialogue where emotions trigger state transitions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.6, 'jeza')
    lines.append(f"{agent1.name} čuti jezo. Napetost: {agent1.tension:.1f}")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.8, 'veselje')
    lines.append(f"{agent2.name} čuti veselje. Napetost: {agent2.tension:.1f}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
