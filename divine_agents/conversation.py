from typing import List
from .agent import Agent


class ConversationManager:
    """Manage dialogues between agents with memory and dynamic updates."""

    def __init__(self, agent1: Agent, agent2: Agent) -> None:
        self.agents = [agent1, agent2]
        self.history: List[str] = []

    def _record(self, line: str) -> None:
        """Store a line in conversation history."""
        self.history.append(line)

    def exchange(self, speaker_index: int, question: str) -> str:
        """Handle a single exchange from one agent."""
        speaker = self.agents[speaker_index]
        response = speaker.respond(question)
        self._record(f"{speaker.name} ({speaker.state}): {response}")
        # update emotion and tension slightly
        speaker.update_emotion(min(1.0, speaker.emotion + 0.1))
        speaker.update_tension(min(1.0, speaker.tension + 0.1))
        speaker.transition()
        return response

    def run_conversation(self, questions: List[str]) -> List[str]:
        """Run conversation with alternating agents."""
        for idx, question in enumerate(questions):
            self.exchange(idx % 2, question)
        return self.history
