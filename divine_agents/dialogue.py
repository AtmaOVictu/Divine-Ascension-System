from typing import List
from .agent import Agent
from .intensity import Intensity


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # intensity objects for visualising tension
    inten1 = Intensity(state="stabilnost")
    inten2 = Intensity(state="stabilnost")
    lines.append(inten1.increase())
    lines.append(inten2.increase())

    # update emotional state and display intensity
    agent1.update_emotion(0.8)
    inten1.state = "visoka napetost"
    lines.append(inten1.increase())
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    inten2.state = "prehod"
    lines.append(inten2.increase())
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final responses
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
