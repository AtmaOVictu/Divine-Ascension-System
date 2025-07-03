from typing import List, Tuple
import threading
from .agent import Agent

dialogue_lock = threading.Lock()


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines: List[str] = []
    with dialogue_lock:
        lines.append(
            f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}"
        )
        lines.append(
            f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}"
        )

        agent1.set_emotion("jeza", 0.8)
        lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

        agent2.set_emotion("veselje", 0.6)
        lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

        lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
        lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


def run_parallel_dialogues(pairs: List[Tuple[Agent, Agent]]) -> List[List[str]]:
    """Run multiple dialogues in parallel using threads."""
    results: List[List[str]] = []

    def worker(a1: Agent, a2: Agent) -> None:
        res = philosophical_dialogue(a1, a2)
        results.append(res)

    threads = [threading.Thread(target=worker, args=p) for p in pairs]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return results
