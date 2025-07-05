from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    Emotions are updated during the conversation which may trigger state
    transitions. The resulting lines capture the philosophical standpoint and
    current emotional tone of each agent.
    """

    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotions rise during the debate
    agent1.update_emotion(0.8, "anger")
    lines.append(
        f"{agent1.name} čuti jezo. Tenzija: {agent1.tension:.1f}."
    )
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, "joy")
    lines.append(
        f"{agent2.name} občuti veselje. Tenzija: {agent2.tension:.1f}."
    )
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Concluding statements after potential transitions
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    return lines
