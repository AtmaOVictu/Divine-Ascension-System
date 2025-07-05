from typing import List

from .agent import Agent


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


def philosophical_debate(agent1: Agent, agent2: Agent, turns: int = 3) -> List[str]:
    """Run a multi-turn philosophical debate between two agents.

    Emotions increase with each turn which may trigger state transitions.
    Returns the dialogue lines generated during the debate.
    """
    debate_lines: List[str] = []
    for _ in range(turns):
        debate_lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        debate_lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Increase emotional intensity to potentially trigger a state change.
        agent1.update_emotion(agent1.emotion + 0.6)
        agent1.transition()

        agent2.update_emotion(agent2.emotion + 0.6)
        agent2.transition()

    return debate_lines
