from typing import List
from .agent import Agent
from .ontology import OntologicalLibrary


def philosophical_dialogue(agent1: Agent, agent2: Agent) -> List[str]:
    """Simulate a short philosophical dialogue between two agents."""
    lines = []
    lines.append(f"{agent1.name} ({agent1.state}): {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name} ({agent2.state}): {agent2.respond('Kaj je resnica?')}")

    agent1.update_emotion(0.8)
    lines.append(f"{agent1.name} prehaja v stanje: {agent1.transition()}")

    agent2.update_emotion(0.6)
    lines.append(f"{agent2.name} prehaja v stanje: {agent2.transition()}")

    lines.append(f"{agent1.name}: {agent1.respond('Kaj je resnica?')}")
    lines.append(f"{agent2.name}: {agent2.respond('Kaj je resnica?')}")
    return lines


class PhilosophicalDebate:
    """Handle a multi-turn debate between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent, library: OntologicalLibrary | None = None) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.library = library or OntologicalLibrary()

    def run(self) -> List[str]:
        """Run the debate and return the conversation lines."""
        lines = []
        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}")

        # escalate emotions triggering potential transitions
        self.agent1.update_emotion(0.8)
        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")

        self.agent2.update_emotion(0.6)
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        lines.append(f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}")
        lines.append(f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}")

        # showcase interaction between terms
        lines.append(self.library.transition_term("Veselje"))
        return lines
