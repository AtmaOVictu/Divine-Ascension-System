import asyncio
import random
from typing import List

from .agent import Agent

async def asynchronous_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3, delay: float = 0.1) -> List[str]:
    """Run an asynchronous philosophical debate between two agents.

    During each round both agents respond according to their ontological
    state. Their emotions are slightly increased which may trigger
    state transitions based on the thresholds defined in ``Agent``.
    The function returns the lines of dialogue.
    """
    dialogue: List[str] = []
    for _ in range(rounds):
        dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # Randomly adjust emotions to increase tension
        agent1.update_emotion(random.uniform(0.2, 0.4))
        agent2.update_emotion(random.uniform(0.2, 0.4))

        dialogue.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
        dialogue.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
        await asyncio.sleep(delay)
    return dialogue
