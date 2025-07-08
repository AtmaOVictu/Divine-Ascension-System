from typing import List

from .agent import Agent
from .language_module import LanguageModule


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    lang1 = LanguageModule(agent1)
    lang2 = LanguageModule(agent2)

    lines.append(f"{agent1.name} ({agent1.state}): {lang1.generate_response()}")
    lines.append(f"{agent2.name} ({agent2.state}): {lang2.generate_response()}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {lang1.generate_response()}")
    lines.append(f"{agent2.name}: {lang2.generate_response()}")
    return lines
