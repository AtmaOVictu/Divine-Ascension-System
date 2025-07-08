from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical debate between two agents."""
    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Update emotions based on the dialogue
    agent1.update_emotion('jeza', 0.8)
    lines.append(f"{agent1.name} občuti {agent1.emotion_label} in ima napetost {agent1.tension:.1f}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion('veselje', 0.6)
    lines.append(f"{agent2.name} občuti {agent2.emotion_label} in ima napetost {agent2.tension:.1f}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
