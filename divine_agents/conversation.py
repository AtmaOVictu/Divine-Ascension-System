from typing import List
from .agent import Agent


def run_debate(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a multi-round philosophical debate between two agents.

    Each round both agents respond according to their ontological state and
    current emotion. Emotions increase slightly every round which may trigger
    state transitions based on predefined thresholds.
    """
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotion to induce potential state changes
        agent1.update_emotion(min(1.0, agent1.emotion + 0.3))
        agent1.transition()

        agent2.update_emotion(min(1.0, agent2.emotion + 0.3))
        agent2.transition()
    return lines
