from typing import List

from .agent import Agent



def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    # Ensure the common concept of "resnica" has a meaning for both agents
    for agent in (agent1, agent2):
        if "resnica" not in agent.language:
            agent.add_word("resnica", "koncept resnice")
    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.world.description}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.world.description}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    lines.append(f"Razlaga besede 'resnica': {agent1.language.meaning_of('resnica')}")
    return lines
