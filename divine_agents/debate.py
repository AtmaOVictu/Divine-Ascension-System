from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate with emotional influence and possible transitions."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # emotions influence tension
    agent1.set_emotion('anger', 0.6)
    lines.append(f"{agent1.name} cuti {agent1.emotion_name}; stanje: {agent1.transition()}")

    agent2.set_emotion('joy', 0.4)
    lines.append(f"{agent2.name} cuti {agent2.emotion_name}; stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines

