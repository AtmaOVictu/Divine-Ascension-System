from typing import List
from .agent import Agent
from .state import AgentState


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements about truth based on the current state.
    lines.append(f"{agent1.name} ({agent1.state.value}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state.value}): {agent2.respond('Kaj je resnica?')}")

    # Emotions rise during the debate which might trigger transitions.
    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition().value}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition().value}")

    # After transitioning (if any), agents reply again from their new standpoint.
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
