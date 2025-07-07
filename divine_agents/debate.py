from typing import List

from .agent import Agent


def dynamic_debate(agent1: Agent, agent2: Agent, steps: int = 3) -> List[str]:
    """Simulate a dynamic philosophical debate between two agents."""
    lines: List[str] = []
    agents = [agent1, agent2]
    for _ in range(steps):
        for speaker in agents:
            listener = agent2 if speaker is agent1 else agent1
            lines.append(
                f"{speaker.name} ({speaker.state}): {speaker.respond('Kaj je resnica?')}"
            )
            change = 0.4 if speaker.state != listener.state else 0.1
            new_emotion = min(1.0, speaker.emotion + change)
            speaker.update_emotion(new_emotion)
            lines.append(f"{speaker.name} prehaja v stanje: {speaker.transition()}")
        lines.append("---")
    return lines
