from typing import List
from .agent import Agent


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


class DialogueManager:
    """Manage monologues and dialogues between ontological agents."""

    def __init__(self, agent1: Agent, agent2: Agent | None = None) -> None:
        self.agent1 = agent1
        self.agent2 = agent2
        self.dialogues: list[tuple[Agent, Agent]] = []
        self.monologues: list[Agent] = []

    def _line(self, agent: Agent, question: str) -> str:
        """Return a formatted line based on the agent's current state."""
        return f"{agent.name} ({agent.state}): {agent.respond(question)}"

    def exchange(self, question: str, e1: float, e2: float) -> List[str]:
        """Perform one exchange and update emotional states.

        Parameters
        ----------
        question:
            Question posed to both agents.
        e1, e2:
            Emotion intensities for agent1 and agent2 that also affect tension.
        """
        lines = [self._line(self.agent1, question), self._line(self.agent2, question)]

        # Update emotions which implicitly modifies tension
        self.agent1.update_emotion(e1)
        self.agent2.update_emotion(e2)

        # Trigger potential state transitions after emotional update
        self.agent1.transition()
        self.agent2.transition()
        return lines

    def conversation(self, questions: List[str], e1: List[float], e2: List[float]) -> List[str]:
        """Run a multi-turn conversation.

        Each step consists of posing ``questions[i]`` to both agents using the
        corresponding emotional intensities ``e1[i]`` and ``e2[i]``.
        """
        lines: List[str] = []
        for q, emo1, emo2 in zip(questions, e1, e2):
            lines.extend(self.exchange(q, emo1, emo2))
        return lines

    # --- New monologue and start methods ---

    def monologue(self, questions: List[str], emotions: List[float]) -> List[str]:
        """Run a self-reflective monologue for ``agent1``."""
        lines: List[str] = []
        for q, emo in zip(questions, emotions):
            lines.append(self._line(self.agent1, q))
            self.agent1.update_emotion(emo)
            self.agent1.transition()
        return lines

    def start_dialogue(self, questions: List[str], e1: List[float], e2: List[float]) -> List[str]:
        """Start and record a dialogue between ``agent1`` and ``agent2``."""
        if self.agent2 is None:
            raise ValueError("agent2 is required for a dialogue")
        self.dialogues.append((self.agent1, self.agent2))
        return self.conversation(questions, e1, e2)

    def start_monologue(self, questions: List[str], emotions: List[float]) -> List[str]:
        """Start a monologue sequence for ``agent1``."""
        self.monologues.append(self.agent1)
        return self.monologue(questions, emotions)
