from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
        f"{agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
        f"{agent2.respond(question)}"
    )

    agent1.update_emotion(0.8, "anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a multi-round philosophical debate with emotional transitions."""
    lines: List[str] = []
    question = "Kaj je resnica?"

    for i in range(rounds):
        lines.append(
            f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
            f"{agent1.respond(question)}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
            f"{agent2.respond(question)}"
        )

        if i == 0:
            agent1.update_emotion(0.8, "anger")
            agent2.update_emotion(0.6, "joy")
        else:
            agent1.update_emotion(0.6, "fear")
            agent2.update_emotion(0.2, "neutral")

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.emotion_type}): "
        f"{agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.emotion_type}): "
        f"{agent2.respond(question)}"
    )
    return lines
