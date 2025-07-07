from typing import List
from .agent import Agent
import asyncio


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "veselje")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    return lines


async def run_demo_loop(agent1: Agent, agent2: Agent) -> None:
    """Interactive REPL for philosophical discussion between two agents."""
    print("Type 'quit' or 'exit' to stop.")
    while True:
        loop = asyncio.get_event_loop()
        question = await loop.run_in_executor(None, input, "Vi: ")
        if question.lower() in {"quit", "exit"}:
            break
        print(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        print(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
        agent1.update_emotion(min(agent1.emotion + 0.1, 1.0), "radovednost")
        agent2.update_emotion(min(agent2.emotion + 0.1, 1.0), "dvom")
        agent1.transition()
        agent2.transition()
