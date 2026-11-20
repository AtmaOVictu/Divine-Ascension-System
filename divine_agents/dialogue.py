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


def philosophical_debate(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a debate where emotions influence transitions."""
    debate = []

    # Initial statements
    debate.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    debate.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate
    agent1.set_emotion('anger', 0.6)
    debate.append(f"{agent1.name} čuti jezo in prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion('joy', 0.8)
    debate.append(f"{agent2.name} čuti veselje in prehaja v stanje: {agent2.transition()}")

    # Second round of statements after transitions
    debate.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    debate.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return debate
