from typing import List
from .agent import Agent
from .symbolic import transition_to_symbol


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(
        f"{agent1.name} prehaja v stanje: {agent1.transition()} "
        f"{transition_to_symbol(agent1.tension, agent1.emotion)}"
    )

    agent2.update_emotion(0.6)
    lines.append(
        f"{agent2.name} prehaja v stanje: {agent2.transition()} "
        f"{transition_to_symbol(agent2.tension, agent2.emotion)}"
    )

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
