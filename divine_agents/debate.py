from typing import List
from .agent import Agent

# Mapping of emotions to tension increments
EMOTION_EFFECTS = {
    "fear": 0.8,
    "joy": 0.3,
    "anger": 0.9,
    "sorrow": 0.6,
}


def apply_emotion(agent: Agent, emotion: str) -> str:
    """Apply an emotion to an agent and trigger a potential state transition."""
    value = EMOTION_EFFECTS.get(emotion, 0.0)
    agent.update_emotion(value)
    return agent.transition()


def philosophical_debate(agent1: Agent, agent2: Agent, emotion1: str, emotion2: str) -> List[str]:
    """Simulate a debate where emotions influence state transitions."""
    lines: List[str] = []
    # Initial statements
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Apply emotions and transitions
    lines.append(f"{agent1.name} čuti {emotion1}.")
    new_state1 = apply_emotion(agent1, emotion1)
    lines.append(f"{agent1.name} prehaja v stanje: {new_state1}")

    lines.append(f"{agent2.name} čuti {emotion2}.")
    new_state2 = apply_emotion(agent2, emotion2)
    lines.append(f"{agent2.name} prehaja v stanje: {new_state2}")

    # Final statements after transition
    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
