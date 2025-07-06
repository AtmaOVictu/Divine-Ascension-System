from typing import List

from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate where agent1 argues absolute truth and agent2 argues
    relative truth. Emotions influence tension and may trigger transitions."""
    lines: List[str] = []

    # Initial statements based on current states
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate
    agent1.update_emotion(0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.4)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again after possible transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj pa ti menis?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj pa ti menis?')}")
    return lines
