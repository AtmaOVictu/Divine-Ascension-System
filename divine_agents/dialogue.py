from typing import List
from concurrent.futures import ProcessPoolExecutor

from .agent import Agent


def _ask(agent: Agent, question: str) -> str:
    """Helper to get agent response for multiprocessing."""
    return f"{agent.name} ({agent.state}): {agent.respond(question)}"


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    question = "Kaj je resnica?"
    lines: List[str] = []

    with ProcessPoolExecutor(max_workers=2) as exe:
        futures = [exe.submit(_ask, a, question) for a in (agent1, agent2)]
        for future in futures:
            lines.append(future.result())

    agent1.update_emotion(agent1.emotion + 0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(agent2.emotion + 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")
    return lines
