from typing import List
from .agent import Agent
from .boxes import SymbolicBox, EmotionalAgent, EmotionalBox


def philosophical_dialogue(agent1: Agent, agent2: Agent, emotion1: str = "anger", emotion2: str = "joy") -> List[str]:
    """Simulate a philosophical dialogue with emotional thresholds."""
    lines: List[str] = []

    # initial philosophical positions
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # process emotions through emotional boxes
    emotional_agent = EmotionalAgent()
    box1 = EmotionalBox(emotion1)
    box1.process_emotion(emotional_agent)
    agent1.update_emotion(0.8 if 'Negative' in box1.status else 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    box2 = EmotionalBox(emotion2)
    box2.process_emotion(emotional_agent)
    agent2.update_emotion(0.8 if 'Negative' in box2.status else 0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # respond again after state changes
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    # track progression with a symbolic box
    task_box = SymbolicBox(stage="∴", data={"task_name": "Dialogue"})
    if task_box.is_valid_transition("∆"):
        task_box.transition("∆", {"phase": "discussion"})
    if task_box.is_valid_transition("⊘"):
        task_box.transition("⊘", {"phase": "conclusion"})
    lines.append(str(task_box))

    return lines
