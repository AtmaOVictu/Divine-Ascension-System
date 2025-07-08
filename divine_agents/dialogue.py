from typing import List
from .agent import Agent
from .language import generate_anagram, create_amalgamation


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Generate a word based on each agent's current emotion
    if agent1.emotion > 0.5:
        word = generate_anagram("anger", seed=1)
        lines.append(f"{agent1.name} tvori anagram: {word}")
    if agent2.emotion > 0.5:
        word = create_amalgamation(agent1.state.lower(), agent2.state.lower())
        lines.append(f"{agent2.name} tvori amalgamacijo: {word}")

    return lines
