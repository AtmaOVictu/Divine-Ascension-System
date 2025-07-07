"""Dialogue helpers for ontological agents."""

from typing import List
import asyncio

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "radost")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


async def philosophical_dialogue_async(agent1: Agent, agent2: Agent) -> List[str]:
    """Asynchronous variant of ``philosophical_dialogue`` using background responses."""
    lines: List[str] = []

    resp1, resp2 = await asyncio.gather(
        agent1.background_respond("Kaj je resnica?"),
        agent2.background_respond("Kaj je resnica?"),
    )
    lines.append(f"{agent1.name} ({agent1.state}): {resp1}")
    lines.append(f"{agent2.name} ({agent2.state}): {resp2}")

    agent1.update_emotion(0.8, "jeza")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "radost")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    resp1, resp2 = await asyncio.gather(
        agent1.background_respond("Kaj je resnica?"),
        agent2.background_respond("Kaj je resnica?"),
    )
    lines.append(f"{agent1.name}: {resp1}")
    lines.append(f"{agent2.name}: {resp2}")
    return lines
