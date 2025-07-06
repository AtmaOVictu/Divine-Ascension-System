import asyncio
from typing import List

from .agent import Agent


async def _process_agent(agent: Agent) -> None:
    """Update emotion and perform state transition asynchronously."""
    agent.update_emotion(0.6)
    await asyncio.sleep(0)
    agent.transition()


async def async_philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Run an asynchronous philosophical debate between two agents."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
        await asyncio.gather(_process_agent(agent1), _process_agent(agent2))
    return lines

