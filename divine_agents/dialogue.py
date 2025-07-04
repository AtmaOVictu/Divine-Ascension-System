from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def dynamic_philosophical_dialogue(agent1: Agent, agent2: Agent, emotion1: tuple, emotion2: tuple) -> List[str]:
    """Run a dialogue where emotions influence transitions.

    Parameters
    ----------
    agent1 : Agent
        First agent in the conversation.
    agent2 : Agent
        Second agent in the conversation.
    emotion1 : tuple
        Pair of emotion name and intensity for agent1.
    emotion2 : tuple
        Pair of emotion name and intensity for agent2.
    """

    lines: List[str] = []
    question = "Kaj je resnica?"

    # Initial responses
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond(question)}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond(question)}")

    # Update emotions and attempt transitions
    agent1.update_emotion(emotion1[1], emotion1[0])
    lines.append(f"{agent1.name} čuti {agent1.emotion_name}")
    agent1.transition()
    lines.append(f"{agent1.name} je zdaj v stanju: {agent1.state}")

    agent2.update_emotion(emotion2[1], emotion2[0])
    lines.append(f"{agent2.name} čuti {agent2.emotion_name}")
    agent2.transition()
    lines.append(f"{agent2.name} je zdaj v stanju: {agent2.state}")

    # Responses after emotional shift
    lines.append(f"{agent1.name}: {agent1.respond(question)}")
    lines.append(f"{agent2.name}: {agent2.respond(question)}")

    return lines
