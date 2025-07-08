from typing import List
from .agent import Agent
from .reputation import ReputationSystem


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Agents express their ontological perspectives and their fame is updated
    through a simple reputation interaction.
    """

    rep = ReputationSystem()
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state} - {agent1.fame_tier()}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state} - {agent2.fame_tier()}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents help each other to increase fame
    rep.interact(agent1, agent2, action="help")

    lines.append(
        f"{agent1.name} ({agent1.fame_tier()}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.fame_tier()}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
