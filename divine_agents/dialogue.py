from typing import List
from .agent import Agent
from .box import SymbolicBox


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    dialogue_box = SymbolicBox(stage="∴", data={"lines": []})

    def add_line(text: str) -> None:
        current = dialogue_box.get_data().setdefault("lines", [])
        current.append(text)
        dialogue_box.update_data({"lines": current})

    add_line(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    add_line(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.set_emotion("anger", 0.8)
    add_line(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.set_emotion("joy", 0.6)
    add_line(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    add_line(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    add_line(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")

    return dialogue_box.get_data()["lines"]
