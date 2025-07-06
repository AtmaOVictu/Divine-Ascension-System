from .agent import Agent
import re

class MemoryAgent(Agent):
    """Agent that remembers past conversations and analyzes sentiment."""

    POSITIVE_WORDS = {"veselje", "ljubezen", "sreca", "radost"}
    NEGATIVE_WORDS = {"strah", "jeza", "zalost"}

    def __init__(self, name: str, state: str = "Ego", tension: float = 0.0, emotion: float = 0.0):
        super().__init__(name, state, tension, emotion)
        self.memory = []

    def remember(self, line: str) -> None:
        """Store a line from conversation."""
        self.memory.append(line)

    def analyze_sentiment(self) -> float:
        """Simple sentiment score based on remembered lines."""
        if not self.memory:
            return 0.0
        score = 0
        for line in self.memory:
            words = re.findall(r"\w+", line.lower())
            for word in words:
                if word in self.POSITIVE_WORDS:
                    score += 1
                if word in self.NEGATIVE_WORDS:
                    score -= 1
        return score / len(self.memory)

    def respond_with_memory(self, question: str) -> str:
        """Respond influenced by analyzed sentiment."""
        base = self.respond(question)
        sentiment = self.analyze_sentiment()
        if sentiment > 0:
            modifier = " Moja pretekla izkusnja je pozitivna."
        elif sentiment < 0:
            modifier = " Moje izkusnje so bile polne izzivov."
        else:
            modifier = ""
        reply = base + modifier
        self.remember(reply)
        return reply
