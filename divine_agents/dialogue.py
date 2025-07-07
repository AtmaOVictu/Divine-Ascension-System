from typing import List
from .agent import Agent
from .emotional_agent import EmotionalAgent
from .thresholds import EmotionalBox


def philosophical_dialogue(agent1: Agent, agent2: Agent, emotion1: str = "joy", emotion2: str = "fear") -> List[str]:
    """Simulate a philosophical dialogue using emotional thresholds."""
    lines: List[str] = []

    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    e_agent = EmotionalAgent()
    box1 = EmotionalBox(emotion1)
    box2 = EmotionalBox(emotion2)

    lines.append(box1.process_emotion(e_agent))
    lines.append(box2.process_emotion(e_agent))

    if box1.status != "Emotion confirmed: Negative":
        agent1.update_emotion(0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    else:
        lines.append(f"{agent1.name} ne more napredovati zaradi čustev.")

    if box2.status != "Emotion confirmed: Negative":
        agent2.update_emotion(0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    else:
        lines.append(f"{agent2.name} ne more napredovati zaradi čustev.")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return lines
