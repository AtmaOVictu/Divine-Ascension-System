from typing import List
from .agent import Agent


def simulate_debate(agent1: Agent, agent2: Agent, iterations: int = 3) -> List[str]:
    """Simulate a philosophical debate between two agents.

    Each iteration agents respond to a question about truth. Their emotional
    intensity increases, influencing tension and potentially triggering state
    transitions. The dialogue reflects the ontological and emotional state of
    each agent.
    """
    lines: List[str] = []
    question = "Kaj je resnica?"
    for _ in range(iterations):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

        agent1.update_emotion(agent1.emotion + 0.3)
        new_state1 = agent1.transition()
        if new_state1 != agent1.history[-2]:
            lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

        agent2.update_emotion(agent2.emotion + 0.3)
        new_state2 = agent2.transition()
        if new_state2 != agent2.history[-2]:
            lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    return lines
