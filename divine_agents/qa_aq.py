"""QA and AQ system enabling recursive questioning for an Agent."""

from typing import List, Tuple

from .agent import Agent


class QAAQSystem:
    """Handle a simple QA/AQ interaction loop with an Agent."""

    def __init__(self, agent: Agent):
        self.agent = agent
        self.qa_history: List[Tuple[str, str]] = []

    def ask_question(self, question: str) -> str:
        """Ask a question to the agent and store the response."""
        answer = self.agent.respond(question)
        self.qa_history.append((question, answer))
        return answer

    def generate_new_question(self, answer: str) -> str:
        """Generate a follow-up question based on the answer."""
        if "napet" in answer or "tension" in answer:
            return "Kako napetost vpliva na tvojo evolucijo?"
        if "relativna" in answer:
            return "Kako odnosi oblikujejo resnico?"
        return "Kaj je prava narava ravnotezja?"

    def interact(self, initial_question: str) -> List[Tuple[str, str]]:
        """Perform a two-step QA/AQ interaction with state transitions."""
        answer = self.ask_question(initial_question)
        # Increase emotion to trigger possible transition
        self.agent.update_emotion(0.8)
        self.agent.transition()
        follow_up = self.generate_new_question(answer)
        self.ask_question(follow_up)
        return self.qa_history
