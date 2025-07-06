from typing import List
import asyncio
import random
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


async def philosophical_dialogue_async(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a philosophical dialogue asynchronously for the given number of rounds."""

    async def speak(agent: Agent) -> str:
        await asyncio.sleep(0)
        return f"{agent.name} ({agent.state}): {agent.respond('Kaj je resnica?')}"

    lines: List[str] = []
    for _ in range(rounds):
        responses = await asyncio.gather(speak(agent1), speak(agent2))
        lines.extend(responses)

        agent1.update_emotion(random.uniform(0.6, 0.9))
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(random.uniform(0.6, 0.9))
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines
