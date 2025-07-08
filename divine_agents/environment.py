from .agent import Agent
from .time_module import TimeModule
from .history_module import HistoryModule
from .space_module import SpaceModule
from .language_module import LanguageModule
from typing import List


def run_simulation() -> List[str]:
    """Run a simple simulation between two agents."""
    time_mod = TimeModule()
    history = HistoryModule()
    space = SpaceModule()

    agent1 = Agent("Agent1")
    agent2 = Agent("Agent2", state="Jaz")

    lang1 = LanguageModule(agent1)
    lang2 = LanguageModule(agent2)

    space.add_agent(agent1.name, (0, 0))
    space.add_agent(agent2.name, (1, 0))

    history.record_event(agent1.name, agent1.state, agent1.emotion)
    history.record_event(agent2.name, agent2.state, agent2.emotion)

    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    # Agents process each other's statements
    lang1.process_input("fear")
    lang2.process_input("joy")

    lines.append(f"{agent1.name} transitions to: {agent1.transition()}")
    lines.append(f"{agent2.name} transitions to: {agent2.transition()}")

    history.record_event(agent1.name, agent1.state, agent1.emotion)
    history.record_event(agent2.name, agent2.state, agent2.emotion)

    time_mod.update_time()
    lines.append(f"Elapsed time: {time_mod.elapsed_time:.2f}s")

    lines.append(f"Distance between agents: {space.distance(agent1.name, agent2.name)}")

    lines.append(f"{agent1.name}: {lang1.generate_reply()}")
    lines.append(f"{agent2.name}: {lang2.generate_reply()}")

    return lines
