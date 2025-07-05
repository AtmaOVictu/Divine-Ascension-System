from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent, rounds: int = 3) -> List[str]:
    """Simulate a dialogue where small NANO events can lead to MEGA transitions."""
    lines: List[str] = []
    for _ in range(rounds):
        lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

        agent1.nano_event(0.2, 0.1)
        agent2.nano_event(0.2, 0.1)

        prev_state1 = agent1.state
        prev_state2 = agent2.state
        new_state1 = agent1.transition()
        new_state2 = agent2.transition()
        lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
        lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

        if agent1.nano_counter == 0 and (prev_state1 != new_state1 or agent1.tension >= 1.0):
            lines.append(f"{agent1.name} doživlja MEGA prehod!")
        if agent2.nano_counter == 0 and (prev_state2 != new_state2 or agent2.tension >= 1.0):
            lines.append(f"{agent2.name} doživlja MEGA prehod!")
    return lines
