from typing import List
from .agent import Agent


def emotional_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a debate where emotions trigger state transitions."""
    lines: List[str] = []

    # initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # agents experience emotions during debate
    agent1.set_emotion('jeza', 0.6)
    agent2.set_emotion('veselje', 0.8)
    lines.append(f"{agent1.name} čuti {agent1.emotion_label} in ima napetost {agent1.tension:.1f}")
    lines.append(f"{agent2.name} čuti {agent2.emotion_label} in ima napetost {agent2.tension:.1f}")

    # possible transitions after emotional surge
    prev_state1 = agent1.state
    prev_state2 = agent2.state
    agent1.transition()
    agent2.transition()
    if agent1.state != prev_state1:
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
    if agent2.state != prev_state2:
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    # agents respond again after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
