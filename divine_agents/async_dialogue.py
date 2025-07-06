import asyncio
from typing import Iterable, List

from .agent import Agent


async def _progress(agent: Agent, increments: Iterable[float]) -> None:
    """Apply emotion increments asynchronously and trigger state transitions."""
    for delta in increments:
        agent.update_emotion(delta)
        agent.transition()
        await asyncio.sleep(0)


async def asynchronous_dialogue(
    agent1: Agent,
    agent2: Agent,
    increments1: Iterable[float] = (0.8,),
    increments2: Iterable[float] = (0.6,),
) -> List[str]:
    """Run a short asynchronous dialogue and return conversation lines."""
    lines = [
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}",
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}",
    ]

    await asyncio.gather(
        _progress(agent1, increments1),
        _progress(agent2, increments2),
    )

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
