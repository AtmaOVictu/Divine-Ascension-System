import asyncio
import random
from typing import List

from .agent import Agent


async def _update_agent(agent: Agent) -> None:
    """Increment emotion and attempt a state transition."""
    delta = random.uniform(0.3, 0.8)
    agent.update_emotion(delta)
    agent.transition()
    await asyncio.sleep(0)


async def async_philosophical_dialogue(agent1: Agent, agent2: Agent, steps: int = 3) -> List[str]:
    """Run an asynchronous philosophical dialogue between two agents."""
    lines: List[str] = []
    for _ in range(steps):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        await asyncio.gather(_update_agent(agent1), _update_agent(agent2))
    return lines
