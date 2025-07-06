from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a dialogue until one of the agents reaches ``Enotnost``."""

    dialogue_lines: List[str] = []
    step = 0
    while agent1.state != "Enotnost" and agent2.state != "Enotnost" and step < 20:
        dialogue_lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        dialogue_lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(0.1)
        agent2.update_emotion(0.1)

        agent1.transition()
        agent2.transition()

        step += 1

    return dialogue_lines
