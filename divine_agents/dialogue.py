from typing import List

from .agent import Agent
from .time_module import TimeModule
from .history_module import HistoryModule
from .space_module import SpaceModule
from .language_module import LanguageModule


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a philosophical dialogue integrating all modules."""

    lines: List[str] = []
    history = HistoryModule()
    timer = TimeModule()
    space = SpaceModule()
    space.add_agent_to_space(agent1.name, (0, 0))
    space.add_agent_to_space(agent2.name, (1, 0))

    lang1 = LanguageModule(agent1)
    lang2 = LanguageModule(agent2)

    # Initial statements about truth
    lines.append(f"{agent1.name} ({agent1.state}): {lang1.generate_response()}")
    lines.append(f"{agent2.name} ({agent2.state}): {lang2.generate_response()}")

    history.record_event(f"{agent1.name} greets {agent2.name}", agent1.emotion, agent1.state)
    timer.update_time()

    # Agent1 reacts to Agent2's relative truth argument
    lang1.process_input("anger")
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")
    history.record_event(f"{agent1.name} transitions", agent1.emotion, agent1.state)
    timer.update_time()

    # Agent2 responds to Agent1's absolutism
    lang2.process_input("fear")
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")
    history.record_event(f"{agent2.name} transitions", agent2.emotion, agent2.state)
    timer.update_time()

    # Closing responses
    lines.append(f"{agent1.name}: {lang1.generate_response()}")
    lines.append(f"{agent2.name}: {lang2.generate_response()}")

    return lines
