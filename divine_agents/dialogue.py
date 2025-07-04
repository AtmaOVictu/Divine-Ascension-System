from typing import List
from .agent import Agent
from .time_utils import get_local_time


def philosophical_dialogue(agent1: Agent, agent2: Agent, question: str = "Kaj je resnica?") -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # emotions influence tension and may trigger transitions
    agent1.update_emotion(0.8, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "strah")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")
    lines.append(f"Čas pogovora: {get_local_time()}")
    return lines
