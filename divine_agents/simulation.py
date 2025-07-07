from typing import List

from .agent import Agent


def dynamic_philosophical_debate(agent1: Agent, agent2: Agent, rounds: int = 2) -> List[str]:
    """Run a debate between two agents with dynamic state transitions.

    Each round the agents respond according to their current ontological state.
    Their emotions are heightened which may trigger state transitions based on
    the defined thresholds.
    """
    dialogue = []
    for idx in range(rounds):
        dialogue.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        dialogue.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        # escalate emotions and check for possible transitions
        agent1.update_emotion(0.6 if idx == 0 else 0.2)
        transition1 = agent1.transition()
        dialogue.append(f"{agent1.name} prehaja v stanje: {transition1}")

        agent2.update_emotion(0.8 if idx == 0 else 0.2)
        transition2 = agent2.transition()
        dialogue.append(f"{agent2.name} prehaja v stanje: {transition2}")

    return dialogue
