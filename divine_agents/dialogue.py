from typing import List, Optional
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotions1: Optional[List[float]] = None,
    emotions2: Optional[List[float]] = None,
    script: Optional[List[str]] = None,
) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    Parameters
    ----------
    agent1 : Agent
        First conversational agent.
    agent2 : Agent
        Second conversational agent.
    emotions1 : list of float, optional
        Emotion values applied to agent1 at each step.
    emotions2 : list of float, optional
        Emotion values applied to agent2 at each step.
    script : list of str, optional
        Questions or prompts used in the dialogue.

    Returns
    -------
    List[str]
        Conversation transcript.
    """

    emotions1 = emotions1 or [0.8]
    emotions2 = emotions2 or [0.6]
    script = script or ["Kaj je resnica?", "Kaj je resnica?"]

    lines: List[str] = []

    # Initial responses
    question = script[0]
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # First emotion update and transition
    if emotions1:
        agent1.update_emotion(emotions1[0])
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    if emotions2:
        agent2.update_emotion(emotions2[0])
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Remaining script interactions
    for i in range(1, len(script)):
        question = script[i]
        lines.append(f"{agent1.name}: {agent1.respond(question)}")
        lines.append(f"{agent2.name}: {agent2.respond(question)}")
        if i < len(emotions1):
            agent1.update_emotion(emotions1[i])
            lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        if i < len(emotions2):
            agent2.update_emotion(emotions2[i])
            lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
