from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotional reactions increase tension and may trigger transitions
    agent1.update_emotion(agent1.emotion + 0.6)
    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent1.name} čuti napetost: {agent1.tension:.1f}")
    lines.append(f"{agent2.name} čuti napetost: {agent2.tension:.1f}")

    new_state1 = agent1.transition()
    new_state2 = agent2.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
