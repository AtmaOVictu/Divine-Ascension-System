from typing import List

from .agent import Agent


class OntologicalDebate:
    """Orchestrate a debate where agents evolve through ontological states."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.rounds = 0
        self.transcript: List[str] = []

    def step(self) -> List[str]:
        """Perform a single step of dialogue and possible transitions."""
        lines = [
            f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond('Kaj je resnica?')}",
            f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond('Kaj je resnica?')}",
        ]

        # escalate emotions and check transitions
        self.agent1.update_emotion(min(self.agent1.emotion + 0.3, 1.0))
        lines.append(f"{self.agent1.name} prehaja v stanje: {self.agent1.transition()}")

        self.agent2.update_emotion(min(self.agent2.emotion + 0.3, 1.0))
        lines.append(f"{self.agent2.name} prehaja v stanje: {self.agent2.transition()}")

        self.transcript.extend(lines)
        self.rounds += 1
        return lines

    def run(self, max_rounds: int = 5) -> List[str]:
        """Run the debate until both agents reach Enotnost or max_rounds."""
        while self.rounds < max_rounds:
            self.step()
            if self.agent1.state == "Enotnost" and self.agent2.state == "Enotnost":
                break
        return self.transcript
