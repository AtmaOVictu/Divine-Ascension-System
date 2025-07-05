from typing import List
from .agent import Agent


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue with emotional transitions."""
    lines: List[str] = []

    # Opening statements
    lines.append(agent1.speak("Kaj je resnica?"))
    lines.append(agent2.speak("Kaj je resnica?"))

    # First emotional reactions
    agent1.update_emotion("anger", 0.6)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion("joy", 0.4)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Second round of discussion
    lines.append(agent1.speak("Kaj pa zdaj misliš o resnici?"))
    agent1.update_emotion("joy", 0.5)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    lines.append(agent2.speak("Kako ti vidiš resnico?"))
    agent2.update_emotion("sorrow", 0.7)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    # Final statements
    lines.append(agent1.speak("Zaklju\u010dek?"))
    lines.append(agent2.speak("Zaklju\u010dek?"))

    return lines
