from typing import List
from .agent import Agent
from .language import LanguageModel


def philosophical_dialogue(
    agent1: Agent,
    agent2: Agent,
    lang1: LanguageModel | None = None,
    lang2: LanguageModel | None = None,
) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""

    lines: List[str] = []

    lines.append(
        f"{agent1.name} ({agent1.state}, {agent1.language.name}): "
        f"{agent1.respond('Kaj je resnica?')}"
    )
    lines.append(
        f"{agent2.name} ({agent2.state}, {agent2.language.name}): "
        f"{agent2.respond('Kaj je resnica?')}"
    )

    if lang1 is not None:
        lines.append(agent1.change_language(lang1))
    if lang2 is not None:
        lines.append(agent2.change_language(lang2))

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines
