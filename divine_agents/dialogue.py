from typing import List
from .agent import Agent
from .ontology import validate, oppose, invalidate


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(
        f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
    )

    agent1.update_emotion(0.8, emotion_type="fear")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6, emotion_type="joy")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # Demonstrate ontological operations on their tension values
    lines.append(
        f"validacija({agent1.tension:.1f}) = {validate(agent1.tension, 2):.2f}"
    )
    lines.append(f"nasprotje({agent2.tension:.1f}) = {oppose(agent2.tension):.2f}")
    lines.append(
        f"invalidacija({agent2.tension:.1f}) = {invalidate(agent2.tension):.2f}"
    )
    return lines
