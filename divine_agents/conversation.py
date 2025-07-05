from typing import List

from .agent import Agent


class DialogueSession:
    """Manage a philosophical dialogue between two agents."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.history: List[str] = []

    def exchange(self, emotion1: float, emotion2: float, question: str = "Kaj je resnica?") -> List[str]:
        """Execute one exchange of dialogue and update states."""
        line1 = f"{self.agent1.name} ({self.agent1.state}): {self.agent1.respond(question)}"
        line2 = f"{self.agent2.name} ({self.agent2.state}): {self.agent2.respond(question)}"
        self.history.extend([line1, line2])

        self.agent1.update_emotion(emotion1)
        self.agent2.update_emotion(emotion2)
        new_state1 = self.agent1.transition()
        new_state2 = self.agent2.transition()

        state_line1 = f"{self.agent1.name} prehaja v stanje: {new_state1}"
        state_line2 = f"{self.agent2.name} prehaja v stanje: {new_state2}"
        self.history.extend([state_line1, state_line2])

        return [line1, line2, state_line1, state_line2]

    def run(self, emotions1: List[float], emotions2: List[float]) -> List[str]:
        """Run multiple exchanges with provided emotion sequences."""
        for e1, e2 in zip(emotions1, emotions2):
            self.exchange(e1, e2)
        return self.history
