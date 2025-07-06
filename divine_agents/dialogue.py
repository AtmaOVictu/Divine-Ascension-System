from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial positions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional reactions to the first statements
    agent1.update_emotion("anger", 0.6)
    agent2.update_emotion("joy", 0.4)
    lines.append(f"{agent1.name} čuti jezo. Napetost: {agent1.tension:.1f}")
    lines.append(f"{agent2.name} čuti veselje. Napetost: {agent2.tension:.1f}")

    # Possible state transitions triggered by emotion/tension
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Agents respond again from their (possibly) new states
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kako vidiš resnico?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kako vidiš resnico?')}"
    )
    return lines
