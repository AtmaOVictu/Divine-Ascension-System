from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial views
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise after hearing the other's argument
    agent1.set_emotion("anger", 0.6)
    lines.append(f"{agent1.name} cuti {agent1.emotion_type}.")
    lines.append(f"{agent1.name} ostaja v: {agent1.transition()}")

    agent2.set_emotion("joy", 0.4)
    lines.append(f"{agent2.name} cuti {agent2.emotion_type}.")
    lines.append(f"{agent2.name} ostaja v: {agent2.transition()}")

    # Tension continues to build
    agent1.set_emotion("radovednost", 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("zaskrbljenost", 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections based on new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
