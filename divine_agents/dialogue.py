from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Run a simple dialogue and update emotional states.

    Both agents start in their current states, exchange their views on truth
    and then react emotionally to each other's claims. Emotions raise tension
    and may cause a transition to the next ontological level.
    """

    lines: List[str] = []

    # Initial statements based on current state.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Reaction phase - emotions affect tension and trigger transitions.
    agent1.update_emotion(0.8, 'anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, 'presenečenje')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements after possible transitions.
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    return lines
