from typing import Iterable, List

from .agent import Agent


def philosophical_debate(
    agent1: Agent,
    agent2: Agent,
    emotions1: Iterable[float],
    emotions2: Iterable[float],
    question: str = "Kaj je resnica?",
) -> List[str]:
    """Simulate a multi-round philosophical debate.

    Each agent receives an emotion update per round. The emotion value is added
    to the agent's tension via :func:`Agent.update_emotion`. After the update
    a response is generated and a potential state transition occurs.
    The dialogue lines along with the new states are returned.
    """
    lines: List[str] = []
    for e1, e2 in zip(emotions1, emotions2):
        agent1.update_emotion(e1)
        agent2.update_emotion(e2)

        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.transition()
        agent2.transition()

        lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")
        lines.append(f"{agent1.name}: {agent1.respond(question)}")
        lines.append(f"{agent2.name}: {agent2.respond(question)}")
    return lines
