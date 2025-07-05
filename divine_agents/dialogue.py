from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue influenced by agents' emotions."""
    dialogue: List[str] = []

    # Agent 1 responds and transitions based on fear
    message1 = "To je zelo pomembno vprašanje."
    agent1.update_emotion(0.8, "strah")
    dialogue.append(agent1.response_with_emotion(message1))
    agent1.transition()

    # Agent 2 responds with joy and transitions as well
    message2 = "Mogoče res, vendar vedno obstaja rešitev."
    agent2.update_emotion(0.9, "veselje")
    dialogue.append(agent2.response_with_emotion(message2))
    agent2.transition()

    return dialogue
