from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Simulate a philosophical dialogue between two agents.

    The dialogue proceeds in rounds where each agent responds to the question
    "Kaj je resnica?". After every exchange their emotion is slightly increased
    to trigger possible state transitions.
    """

    lines: List[str] = []
    for _ in range(rounds):
        lines.append(agent1.speak("Kaj je resnica?"))
        lines.append(agent2.speak("Kaj je resnica?"))

        agent1.update_emotion(agent1.emotion + 0.4)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.update_emotion(agent2.emotion + 0.4)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final reflections
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))
    return lines
