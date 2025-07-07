from typing import List
from .agent import Agent
from .lock import Lock


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with emotional influence."""
    lines = []
    question = "Kaj je resnica?"

    # initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # add locks controlling state transitions
    agent1.add_lock(Lock("state_lock1", condition="emotion", threshold=0.5))
    agent2.add_lock(Lock("state_lock2", condition="tension", threshold=0.7))

    # update emotional states
    agent1.update_emotion(0.6)
    agent2.update_tension(0.8)

    # attempt transitions
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # final responses after transition
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")
    return lines
