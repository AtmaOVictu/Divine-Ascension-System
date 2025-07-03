from typing import List
from .agent import Agent

class SyntaxAgent(Agent):
    """Agent with syntax-based procedures for state transitions."""

    def syntax_procedure(self, emotion: float, tension: float) -> str:
        """Update internal emotion and tension then attempt a state transition."""
        self.update_emotion(emotion)
        self.update_tension(tension)
        return self.transition()


def create_syntax_agents(count: int) -> List[SyntaxAgent]:
    """Create a list of SyntaxAgent instances."""
    return [SyntaxAgent(f"Syntax-{i}") for i in range(1, count + 1)]
