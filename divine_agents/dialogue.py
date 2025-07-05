from typing import List

from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue using complex transitions."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    state1, err1 = agent1.complex_transition(interactions=0.3, environment=0.1)
    lines.append(f"{agent1.name} prehaja v stanje: {state1} (napaka: {err1:.2f})")

    agent2.update_emotion(0.6)
    state2, err2 = agent2.complex_transition(interactions=0.3, environment=0.1)
    lines.append(f"{agent2.name} prehaja v stanje: {state2} (napaka: {err2:.2f})")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
