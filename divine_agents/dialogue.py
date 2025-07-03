"""Tools for simulating philosophical discussions between agents."""

from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements based on current states.
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions increase tension and may cause transitions.
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after potential transitions.
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a two-turn debate showing how emotions trigger transitions."""
    transcript = philosophical_dialogue(agent1, agent2)

    # Second round with moderate emotional changes.
    agent1.update_emotion(0.4)
    transcript.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.4)
    transcript.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    transcript.append(f"{agent1.name}: {agent1.respond('Ali so resnice zdruzene?')}")
    transcript.append(f"{agent2.name}: {agent2.respond('Ali so resnice zdruzene?')}")
    return transcript
