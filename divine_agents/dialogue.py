from typing import List, Optional
from .agent import Agent
from .network import SharedMemory


def philosophical_dialogue(agent1: Agent, agent2: Agent, memory: Optional[SharedMemory] = None) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")
    if memory:
        memory.record_event(f"dialogue start between {agent1.name} and {agent2.name}")

    agent1.update_emotion(0.8)
    new_state1 = agent1.transition()
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")
    if memory:
        memory.record_event(f"{agent1.name} transitioned to {new_state1}")

    agent2.update_emotion(0.6)
    new_state2 = agent2.transition()
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")
    if memory:
        memory.record_event(f"{agent2.name} transitioned to {new_state2}")

    reply1 = agent1.respond('Kaj je resnica?')
    reply2 = agent2.respond('Kaj je resnica?')
    lines.append(f"{agent1.name}: {reply1}")
    lines.append(f"{agent2.name}: {reply2}")
    if memory:
        memory.record_event(f"{agent1.name} said: {reply1}")
        memory.record_event(f"{agent2.name} said: {reply2}")
    return lines
