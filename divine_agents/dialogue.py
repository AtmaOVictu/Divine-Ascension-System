from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Agents express their view of truth based on their ontological state and
    emotions.  After the initial exchange emotions are increased which may
    trigger a state transition.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.colour}): {agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.colour}): {agent2.respond(question)}"
    )

    # Increase emotions to provoke transitions
    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} ({agent1.colour}, {agent1.visibility})"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} ({agent2.colour}, {agent2.visibility})"
    )

    # Second round after transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond(question)}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond(question)}"
    )

    return lines
