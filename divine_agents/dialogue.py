from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []

    # Initial statements based on current ontological states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise as debate unfolds
    agent1.set_emotion("anger", 0.6)
    lines.append(f"{agent1.name} čuti {agent1.emotion_type}.")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("joy", 0.7)
    lines.append(f"{agent2.name} čuti {agent2.emotion_type}.")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final reflections after transitions
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
