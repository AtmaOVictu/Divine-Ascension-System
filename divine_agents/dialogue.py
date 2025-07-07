from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents.

    The function updates the emotional state of each agent which may trigger
    state transitions. Returned lines capture the progression of the debate.
    """
    lines: List[str] = []

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agent2 challenges Agent1 causing anger which increases tension
    agent1.update_emotion(0.8, 'anger')
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    # Agent2 stays calm but also gains slight emotion leading to possible shift
    agent2.update_emotion(0.6, 'calm')
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # After transitions they respond again reflecting new states
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
