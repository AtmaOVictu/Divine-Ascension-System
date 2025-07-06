from typing import List
from concurrent.futures import ThreadPoolExecutor

from .agent import Agent


def _response_line(agent: Agent, question: str) -> str:
    """Compose a single response line for the given agent."""
    return f"{agent.name} ({agent.state}): {agent.respond(question)}"


def parallel_responses(agents: List[Agent], question: str) -> List[str]:
    """Return agent responses in parallel using threads."""
    with ThreadPoolExecutor(max_workers=len(agents)) as executor:
        return list(executor.map(lambda a: _response_line(a, question), agents))


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = parallel_responses([agent1, agent2], "Kaj je resnica?")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.extend(parallel_responses([agent1, agent2], "Kaj je resnica?"))
    return lines
