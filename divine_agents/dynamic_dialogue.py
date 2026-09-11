from typing import List

from .agent import Agent


def dynamic_philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a short debate where emotions drive state transitions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotion influences
    agent1.apply_emotion('anger', 0.6)
    lines.append(f"{agent1.name} \u010duti jezo in napetost {agent1.tension:.1f}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.apply_emotion('joy', 0.8)
    lines.append(f"{agent2.name} \u010duti veselje in napetost {agent2.tension:.1f}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines
