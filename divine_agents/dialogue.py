from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotional shifts increase tension and may trigger state transitions.
    """
    lines: List[str] = []

    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents experience emotions which raise tension
    agent1.set_emotion("jeza", 0.8)
    lines.append(f"{agent1.name} čuti jezo, napetost {agent1.tension:.2f}")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("strah", 0.8)
    lines.append(f"{agent2.name} čuti strah, napetost {agent2.tension:.2f}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Further escalation to reach a higher state
    agent2.set_emotion("strah", 0.8)
    lines.append(f"{agent2.name} čuti strah, napetost {agent2.tension:.2f}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements influenced by current states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
