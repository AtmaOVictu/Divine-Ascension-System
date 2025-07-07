from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines

from .boxes import SymbolicBox, EmotionalBox
from .emotional import EmotionalAgent


def threshold_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Dialogue using symbolic and emotional thresholds."""
    lines: List[str] = []
    box = SymbolicBox(stage="∴", data={"topic": "Kaj je resnica?"})
    ebox1 = EmotionalBox("fear")
    ebox2 = EmotionalBox("joy")
    emotion_agent = EmotionalAgent("EA")

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    ebox1.process_emotion(emotion_agent)
    ebox2.process_emotion(emotion_agent)

    agent1.update_emotion(0.8)
    agent2.update_emotion(0.6)

    if box.is_valid_transition("∆"):
        box.transition("∆", {agent1.name: agent1.transition(), agent2.name: agent2.transition()})
    lines.append(str(box))

    return lines
