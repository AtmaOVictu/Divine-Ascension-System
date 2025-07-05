from typing import List
from .agent import Agent


def philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical debate between two agents."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.update_emotion(agent1.emotion + 0.6, emotion_type="jeza")
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.6, emotion_type="radost")
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    return lines


# Backward compatibility for existing tests
def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    return philosophical_debate(agent1, agent2, rounds=1)
