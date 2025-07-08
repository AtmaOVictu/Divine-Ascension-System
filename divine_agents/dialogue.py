from typing import List

from .agent import Agent
from .time_module import TimeModule
from .history_module import HistoryModule
from .space_module import SpaceModule
from .language_module import LanguageModule


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue integrating helper modules."""

    time_mod = TimeModule()
    history = HistoryModule()
    space = SpaceModule()
    lang1, lang2 = LanguageModule(agent1), LanguageModule(agent2)

    space.add_agent_to_space(agent1.name, (0, 0))
    space.add_agent_to_space(agent2.name, (1, 0))

    lines: List[str] = []
    lines.append(f"{agent1.name} ({agent1.state}): {lang1.generate_response()}")
    lines.append(f"{agent2.name} ({agent2.state}): {lang2.generate_response()}")

    lang1.process_input("angry")
    agent1.transition()
    history.record_event("transition", agent1.state, "")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.state}")

    lang2.process_input("angry")
    agent2.transition()
    history.record_event("transition", agent2.state, "")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.state}")

    lines.append(f"Proximity: {space.check_proximity(agent1.name, agent2.name)}")
    lines.append(f"Elapsed: {time_mod.update_time():.2f}s")
    lines.append(f"{agent1.name}: {lang1.generate_response()}")
    lines.append(f"{agent2.name}: {lang2.generate_response()}")

    history.record_event("end", agent1.state, agent2.state)
    return lines
