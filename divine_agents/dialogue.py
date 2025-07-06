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


def debate(agent1: Agent, agent2: Agent, topic: str = "Kaj je resnica?") -> List[str]:
    """Run a debate where emotions influence state transitions."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")

    agent1.update_emotion(0.6, "anger")
    lines.append(
        f"{agent1.name} čuti {agent1.emotion_type}. Prehod: {agent1.transition()}"
    )

    agent2.update_emotion(0.4, "joy")
    lines.append(
        f"{agent2.name} čuti {agent2.emotion_type}. Prehod: {agent2.transition()}"
    )

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(topic)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(topic)}")
    return lines
