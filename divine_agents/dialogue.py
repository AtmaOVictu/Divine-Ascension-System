from typing import List
from .agent import Agent

EMOTION_TENSION = {
    "fear": 0.3,
    "joy": 0.1,
    "anger": 0.4,
    "sorrow": 0.2,
}


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []

    # Initial statements with current emotion and state
    lines.append(
        f"{agent1.name} [{agent1.emotion_name or 'neutral'}] ({agent1.state}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} [{agent2.emotion_name or 'neutral'}] ({agent2.state}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    # Apply emotions which influence tension differently
    agent1_emotion = "fear"
    agent1_intensity = 0.8
    agent1.update_emotion(agent1_intensity, agent1_emotion)
    agent1.tension += EMOTION_TENSION.get(agent1_emotion, 0.0)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2_emotion = "joy"
    agent2_intensity = 0.6
    agent2.update_emotion(agent2_intensity, agent2_emotion)
    agent2.tension += EMOTION_TENSION.get(agent2_emotion, 0.0)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Responses after emotional shift
    lines.append(
        f"{agent1.name} [{agent1.emotion_name}]: {agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} [{agent2.emotion_name}]: {agent2.respond('Kaj je resnica?')}"
    )

    return lines
