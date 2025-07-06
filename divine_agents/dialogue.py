from typing import List
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


async def philosophical_dialogue_async(agent1: Agent, agent2: Agent) -> List[str]:
    """Asynchronous version of :func:`philosophical_dialogue`."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {await agent1.respond_async('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {await agent2.respond_async('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {await agent1.transition_async()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {await agent2.transition_async()}")

    lines.append(f"{agent1.name}: {await agent1.respond_async('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {await agent2.respond_async('Kaj je resnica?')}")
    return lines
