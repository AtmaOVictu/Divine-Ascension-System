from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a short philosophical debate between two agents."""

    question = "Kaj je resnica?"
    lines: List[str] = []

    # Initial statements reflecting each agent's state
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Emotion escalation influences tension and potential transitions
    agent1.update_emotion(agent2.emotion + 0.4)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent1.emotion + 0.2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final responses after transitions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    return lines
