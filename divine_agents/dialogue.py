from typing import List
from .agent import Agent
from .intensity import Intensity


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents with intensity."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # setup intensity objects reflecting current tension level
    i1 = Intensity('visoka napetost' if agent1.tension > 0.7 else 'stabilnost')
    i2 = Intensity('visoka napetost' if agent2.tension > 0.7 else 'stabilnost')

    color1 = i1.increase()
    lines.append(i1.display(color1))
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    color2 = i2.increase()
    lines.append(i2.display(color2))
    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
