from typing import List
from .agent import Agent


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    emotion1: float = 0.8,
    tension1: float = 0.0,
    emotion2: float = 0.6,
    tension2: float = 0.0,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The emotion and tension values for each agent can be customised via
    parameters. Emotion updates also affect the agent's tension while the
    explicit tension parameters are added on top of that value.
    """
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(emotion1)
    agent1.update_tension(agent1.tension + tension1)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(emotion2)
    agent2.update_tension(agent2.tension + tension2)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
