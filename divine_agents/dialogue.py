from typing import List
from .agent import Agent


def transition_to_symbol(tension: float, emotion: float) -> str:
    """Translate numeric values into an ontological symbol."""
    if tension > 0.7 or emotion > 0.5:
        if tension > emotion:
            return "⊕ (Transcendence - Ego to Jaz)"
        return "⊗ (Balance - Jaz to Enotnost)"
    return "No transition"


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements
    lines.append(
        f"{agent1.name} ({agent1.symbol}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.symbol}): {agent2.respond('Kaj je resnica?')}"
    )

    # Emotional changes influence tension and possible transitions
    agent1.update_emotion(0.8)
    symbol = transition_to_symbol(agent1.tension, agent1.emotion)
    agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state} [{symbol}]")

    agent2.update_emotion(0.6)
    symbol = transition_to_symbol(agent2.tension, agent2.emotion)
    agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state} [{symbol}]")

    # Second round of statements after transitions
    lines.append(
        f"{agent1.name} ({agent1.symbol}): {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.symbol}): {agent2.respond('Kaj je resnica?')}"
    )
    return lines
